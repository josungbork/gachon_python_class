# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup # beautifulSoup 모듈 호출

url = "http://finance.naver.com/item/main.nhn?code=005930"
html = urllib.urlopen(url)
soup = BeautifulSoup(html, "lxml")

dl_tags = soup.find_all("dl",  attrs={'class':'blind'}) # dl 태그 반환
dd_tags = dl_tags[0].find_all("dd") # dl 태그의 첫번째 값에서 dd 태그 반환

for stock_index in dd_tags:
    print stock_index.get_text() # dd 태그의 값들 반환
