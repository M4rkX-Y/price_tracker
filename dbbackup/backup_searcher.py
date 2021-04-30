import lxml
from bs4 import BeautifulSoup
import requests
import time
from time import sleep 
from dbbackup import backupdb
import re


def addproductama(x):
    headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"} 
    cat = "cpu"
    for i in range(x):
        pn = str(i)
        url = "https://www.amazon.com/s?k=" + cat + "&page=" + pn
        page = requests.get(url, headers = headers).text 
        soup = BeautifulSoup(page,"lxml")
        info = soup.find("div", class_="s-main-slot s-result-list s-search-results sg-row")
        if info == None:
            print("error")
        else:
            for col in info.find_all("div", class_="s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16"):
                link = "http://amazon.com" + col.find("a", class_="a-link-normal a-text-normal")['href']
                name = col.find("span", class_="a-size-medium a-color-base a-text-normal").text
                backupdb.add_product(name, link)             


addproductama(20)