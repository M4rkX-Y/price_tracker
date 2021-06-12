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


def refresh(user_agent, url):
    headers = {"User-Agent": user_agent, "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 
#making a list of different headers and randomize it
    page = requests.get(url, headers = headers).text 
    soup = BeautifulSoup(page,"lxml")
    check1 = soup.find("div", class_="page-content")
    check2 = soup.find("div", id="container")
    title, availability, price, check = None, None, None, False
    if check1 is None:
        if check2 is None:
            print("error")
            check = True
        else:
            pr = check2.find("div", class_="wrapper")
            title = pr.find("span", itemprop="name").text
            bb = check2.find("div", class_="grpOptions")
            p = bb.find("div", class_="current")['content']
            price = float(p.replace(",", ""))
            availability = False
            print("done")
    else:
        bb = check1.find("div", class_="product-buy-box")
        if bb is not None:
            check3 = bb.find("li", class_="price-current")
            if check3 is None:
                print("error")
                check = True
            else:
                p = " ".join(bb.find("li", class_="price-current").text.replace("$","").split())
                price = float(p.replace(",", ""))
                pr = check1.find("div", class_="product-wrap")
                title = pr.find("h1", class_="product-title").text
                ava = pr.find("div", class_="product-inventory").text
                arr1 = re.search("^In *", ava)
                if arr1:
                    availability = True
                else:
                    availability = False
                print("done")
        else:
            print("done")
    return title, availability, price, check

def bot_refresh():
    links = cpudb.get_nwe_url()
    error_count = 0
    for index, link in enumerate(links):
        print("Newegg: {} /176".format(index+1))
        id = link[0]
        url = link[1]
        user_agent = ua_randomize()
        title, new_availability, new_price, check = refresh(user_agent, url)
        if check is True:
            error_count = error_count+1
            cpudb.update_nwe_time(id)
        else:
            price_change(id, title, new_price)
            ava_change(id, title, new_availability)
            cpudb.update_nwe_cpu(new_availability, new_price, id)
        sleep(2)
    error = "Newegg Finished, with {} blocks".format(error_count)
    print(error)
    print("---------------------------------------------------------")
    if error_count != 0:
        cpudb.add_error_log(error, "nwe")

def price_change(id, title, new_price):
    pricelist = cpudb.get_nwe_price(id)
    price2 = pricelist[0]
    old_price = price2[0]
    if old_price is not None and new_price is not None and new_price != old_price:
        d1 = cpudb.get_nwe_time(id)
        d2 = d1[0]
        date = d2[0]
        cpudb.add_log(title, old_price, "nwe", date)

def ava_change(id, title, new_availability):
    old_availability = cpudb.get_nwe_ava(id)
    if old_availability == [('1',)] and new_availability == False:
        print(title, "no longer in stock")
    if old_availability == [('0',)] and new_availability == True:
        print(title, "is back in stock")

