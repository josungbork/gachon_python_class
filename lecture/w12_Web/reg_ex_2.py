# -*- coding: utf-8 -*-

import urllib # urllib 모듈 호출
import re

url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html" #url 값 입력
html = urllib.urlopen(url)	 # url 열기
html_contents = str(html.read())  # html 파일 읽고, 문자열로 변환


url_list = re.findall(r"(http)(.+)(zip)", html_contents)

for url in url_list: print type(url)
