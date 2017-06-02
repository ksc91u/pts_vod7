#!/bin/env python
from bs4 import BeautifulSoup
import urllib3
import urllib.parse
import subprocess


def listPrograms(pageUrl):
    http = urllib3.PoolManager()
    r = http.request('GET', pageUrl)
    soup = BeautifulSoup(r.data, "html.parser")
    programs = []
    for anchor in soup.findAll(True, {'class': ['cbp-item']}):
        v = anchor.find_all('li')
        title = anchor.find_all(True, {'class': ['cbp-l-grid-agency-title']})
        # print(title[0].text)
        long_desc = anchor.find_all(True, {'class': ['cbp-l-grid-agency-desc']})
        # print(long_desc[0].text)
        href = v[0].findAll('a', class_="cbp-lightbox", href=True)[0]['href']
        # print(urllib.parse.unquote(href))
        program = {'title': title[0].text, 'desc': long_desc[0].text, 'url': urllib.parse.unquote(href)}
        programs.append(program)
    return programs


def selectPrograms(programs):
    for i in range(programs.__len__()):
        print("%d: %s\n%s\n" % (i, programs[i]['title'], programs[i]['desc']))
    nb = input('numbers: ')
    nums = [int(s) for s in nb.split() if s.isdigit()]
    for j in nums:
        subprocess.call(['ffmpeg', '-i', programs[j]['url'], '-codec', 'copy', programs[j]['title'] + ".mp4"])


programs = listPrograms('http://vod7.pts.org.tw/cate/4#cbpf=.item25')
selectPrograms(programs)
programs = listPrograms('http://vod7.pts.org.tw/cate/5#cbpf=.item29')
selectPrograms(programs)
