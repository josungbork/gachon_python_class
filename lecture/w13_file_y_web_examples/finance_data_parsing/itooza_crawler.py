import code
import urllib
import os 

k_stock_200_file_name = "input/k_stock_200.txt"

stock_codes = []
with open(k_stock_200_file_name,"r") as k_stok_200_file:
    
    while 1:
        line = k_stok_200_file.readline()
        if not line: break
        stock_codes.append(line.strip())


output_prefix = "output"
if not os.path.exists(output_prefix):
        os.makedirs(output_prefix)

web_url_prefix = "http://finance.naver.com/item/main.nhn?code="

for code in stock_codes:
    file_name = output_prefix + code + ".html"
    web_url = web_url_prefix + code
    
    with open(file_name, "w") as stock_html_file:
        html_contents = urllib.urlopen(web_url).read()
        stock_html_file.write(html_contents)
