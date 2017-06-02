#!/bin/env python
from bs4 import BeautifulSoup
import urllib3
import urllib.parse

http = urllib3.PoolManager()
r = http.request('GET', 'http://vod7.pts.org.tw/cate/4#cbpf=.item25')
soup = BeautifulSoup(r.data, "html.parser")

divs = soup.select("div.cbp-l-grid-agency.cbp")
titles = soup.select("div.cbp-l-grid-agency-title")
for anchor in soup.findAll('a', class_="cbp-lightbox", href=True):
    u = anchor['href']
    print(urllib.parse.unquote(u))

found = soup.findAll(True, {'class': ['cbp-item']})
for anchor in soup.findAll(True, {'class': ['cbp-item']}):
    v = anchor.find_all('li')
    title = anchor.find_all(True, {'class': ['cbp-l-grid-agency-title']})
    print(title[0].text)
    long_desc = anchor.find_all(True, {'class':['cbp-l-grid-agency-desc']})
    print(long_desc[0].text)
    href = v[0].findAll('a', class_="cbp-lightbox", href=True)[0]['href']
    print(urllib.parse.unquote(href))
