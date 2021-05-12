import lxml
from bs4 import BeautifulSoup
import requests
import time
from time import sleep 
import schedule
import re
import cpudb
import time
import random  


def ua_randomize():
    user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    ]
    user_agent = random.choice(user_agent_list)
    return user_agent


def refresh(url, user_agent):
    title, availability, price, check = None, None, None, False
    headers = {"User-Agent": user_agent, "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 
    page = requests.get(url, headers = headers).text 
    soup = BeautifulSoup(page,"lxml")
    bb = soup.find('div', id='buybox')
    if bb is not None:
        check = True
        ts = soup.find('div', id='titleSection')
        title = " ".join(ts.find('span', id='productTitle').text.split())
        check_1 = bb.find('div', id='desktop_accordion')
        check_2 = bb.find('div', id='unqualifiedBuyBox')
        check_3 = bb.find('div', id='usedOnlyBuybox')
        check_4 = bb.find('div', id="outOfStock")
        if check_1 is None:
            if check_2 is None:
                if check_3 is None:
                    if check_4 is None:
                        price = " ".join(bb.find('span', id='price_inside_buybox').text.replace("$","").split())
                        ava = " ".join(bb.find('div', id='availability').text.split())
                    else:
                        ava = "False"
                        price = None
                else:   
                    price = " ".join(bb.find('div', id='buyNew_noncbb').text.replace("$","").split())
                    ava = "In Stock."
            else:
                ava = "False"
                price = None
        else:
            ava = " ".join(bb.find('div', id='availability').text.split())
            price = " ".join(check_1.find('span', id='newBuyBoxPrice').text.replace("$","").split())
        arr1 = re.search("^In *", ava)
        arr2 = re.search("^Only.*soon.$", ava)
        if arr1:
            availability = True
        elif arr2:
            availability = True
        else:
            availability = False
    return title, availability, price, check


def bot_refresh():
    links = cpudb.get_amz_url()
    error_count = 0
    for index, link in enumerate(links):
        print(index+1, "/320")
        id = link[0]
        url = link[1]
        user_agent = ua_randomize()
        test = refresh(url, user_agent)
        check = test[3]
        if check is False:
            error_count = error_count+1
            cpudb.update_time("amazon", id)
            print("error")
        else:
            title = test[0]
            new_availability = test[1]
            new_price = test[2]
            
            price_change(id, title, new_price)

            ava_change(id, title, new_availability)

            cpudb.update_amz_cpu(title, new_availability, new_price, id)
            print("done")
            sleep(1)
    error = "Finished, with", error_count, "blocks"
    print(error)
    if error_count != 0:
        cpudb.add_error_log(error, "amz")
    


def price_change(id, title, nprice):
    pricelist = cpudb.get_amz_price(id)
    price2 = pricelist[0]
    oprice = price2[0]
    if oprice is not None and nprice is not None:
        new_price = float(nprice.replace(",",""))
        old_price = float(oprice.replace(",",""))
        if new_price != old_price:
            date = cpudb.get_time("amazon", id)
            cpudb.add_log(title, old_price, "amz", date)

def ava_change(id, title, new_availability):
    old_availability = cpudb.get_amz_ava(id)
    if old_availability == [('1',)] and new_availability == False:
        print(title, "no longer in stock")
    if old_availability == [('0',)] and new_availability == True:
        print(title, "is back in stock")


bot_refresh()