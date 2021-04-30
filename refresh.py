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
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97',
    'Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
    ]
    user_agent = random.choice(user_agent_list)
    return user_agent


def refresh(url, user_agent, error_count):
    headers = {"User-Agent": user_agent, "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 
    page = requests.get(url, headers = headers).text 
    soup = BeautifulSoup(page,"lxml")
    bb = soup.find('div', id='buybox')
    if bb is None:
        error_count = error_count + 1
        print("User agent", user_agent, "got busted")
    else:
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
        print("done")
        return title, availability, price, error_count


def bot_refresh():
    links = cpudb.get_url()
    error_count = 0
    for index, link in enumerate(links):
        print(index+1, "/320 working")
        id = link[0]
        url = link[1]
        user_agent = ua_randomize()
        title, new_availability, new_price, error_count = refresh(url, user_agent, error_count)
        pchange = price_change(id, new_price)
        old_availability = cpudb.get_ava(id)
        if old_availability == [('1',)] and new_availability == False:
            print(title, "no longer in stock")
        if old_availability == [('0',)] and new_availability == True:
            print(title, "is back in stock")
        cpudb.update_cpu(title, new_availability, new_price, id)
        sleep(1)
    print("Finished, with", error_count, "block(s)")


def price_change(id, nprice):
    pricelist = cpudb.get_price(id)
    price2 = pricelist[0]
    oprice = price2[0]
    new_price = float(nprice)
    pchange = new_price - old_price
    return pchange
#still have to work on the logic of this part. Making sure the real time table works and the log table have enough data to plot a graph

bot_refresh()