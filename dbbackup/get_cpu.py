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

def find_amz_url(title, user_agent):
    t = title.replace(" ","+")
    url = "https://www.amazon.com/s?k=" + t + "&i=electronics&ref=nb_sb_noss"
    headers = {"User-Agent": user_agent, "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 
    page = requests.get(url, headers = headers).text 
    soup = BeautifulSoup(page,"lxml")
    info = soup.find("div", class_="s-main-slot s-result-list s-search-results sg-row")
    if info == None:
        print("error")
    else:
        col = info.find("div", class_="s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16")
        link = "http://amazon.com" + col.find("a", class_="a-link-normal a-text-normal")['href']
        return title, link
    
def find_nwe_url(title, user_agent):
    t = title.replace(" ","+")
    url = "https://www.newegg.com/p/pl?d=" + t 
    headers = {"User-Agent": user_agent, "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 
    page = requests.get(url, headers = headers).text 
    soup = BeautifulSoup(page,"lxml")
    info = soup.find("div", class_="row-body-inner")
    if info == None:
        print("error")
    else:
        links = []
        for col in info.find_all("div", class_="item-container"):
            if col is not None:
                link = col.find("a", class_="item-title")['href']
                name = col.find("a", class_="item-title").text
                check1 = re.search("^https://www.newegg.com/Product/ComboDealDetails*", link)
                manuf = re.search("^AMD", title)
                if manuf:
                    check2 = re.search("^AMD", name)
                else:
                    check2 = re.search("^Intel", name)
                if not check1:
                    if check2:
                        links.append(link)
                    else:
                        links.append(None)
        return title, links[0]

def get_cpu():
    for i in range(1,177):
        t = cpudb.get_cpulist(i)
        titles = t[0]
        title = titles[0]
        user_agent = ua_randomize()
        print(i, "/176")
        title, link = find_nwe_url(title, user_agent)
        cpudb.add_nwe_cpu(title, link)
        sleep(2)
    
get_cpu()