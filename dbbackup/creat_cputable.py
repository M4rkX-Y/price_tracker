import lxml
from bs4 import BeautifulSoup
import requests
import time
from time import sleep 
import schedule
import re
from dbbackup import cpudb
from dbbackup import backupdb
import time
import random    

def add_cpu_bot(url):
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
    headers = {"User-Agent": user_agent, "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 
    page = requests.get(url, headers = headers).text 
    soup = BeautifulSoup(page,"lxml")
    bb = soup.find('div', id='buybox')
    if bb is None:
        print("User agent", user_agent, "got busted")
        cpudb.add_cpu(None, url, None, None)
        sleep(1)
    else:
        ts = soup.find('div', id='titleSection')
        title = " ".join(ts.find('span', id='productTitle').text.split())
        check_1 = bb.find('div', id='desktop_accordion')
        check_2 = bb.find('div', id='unqualifiedBuyBox')
        check_3 = bb.find('div', id='usedOnlyBuybox')
        if check_1 is None:
            if check_2 is None:
                if check_3 is None:
                    price = " ".join(bb.find('span', id='price_inside_buybox').text.replace("$","").split())
                    ava = " ".join(bb.find('div', id='availability').text.split())
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
        
        cpudb.add_cpu(title, url, availability, price)
        print("Success")
        sleep(1)

x=1
links = backupdb.backup_url()
for link in links:
    print(x,"/320")
    url = link[0]
    add_cpu_bot(url)
    x=x+1
print("Finished")

