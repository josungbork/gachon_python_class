# -*- coding: utf-8 -*-

import urllib
import re

url = "http://finance.naver.com/item/main.nhn?code=005930"
html = urllib.urlopen(url)
html_contents = str(html.read())

stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_results[0] # 두 개중 첫번째 패턴
samsung_index = samsung_stock[1] # 세 개의 tuple 값중 두 번째 값 
                                 # 하나의 괄호가 tuple index가 됨
index_list= re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)

for index in index_list:
    print index[1].decode("cp949") # 세 개의 tuple 값중 두 번째 값
