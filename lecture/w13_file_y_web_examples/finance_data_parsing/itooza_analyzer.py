# -*- coding: utf-8 -*-

from pip._vendor.html5lib.treewalkers import lxmletree

def getCodeList(file_name):
    f = open(file_name, 'r')
    codelist = []
    while 1: 
        line = str(f.readline()).strip()
        if not line: break 
        codelist.append(line)
    f.close()
    return codelist

def writeFile(file_name, content):
    print file_name

    with open(file_name, 'w') as f:
        f.write(content.encode("utf-8"))
        f.close()

import urllib
import sys
import os
import time
from bs4 import BeautifulSoup



reload(sys)
sys.setdefaultencoding("utf-8")


company_name = ''
financail_items = []
year_quarter_items = []
year_item_data = []
all_data = []

# if (len(sys.argv) < 2):
#     print "Try 'python itooza_analyzer.py input.txt outputForderName'"
#     print "You have to make a Output Forder for storing extracted data."
#     sys.exit()
# sourceFile = sys.argv[1]
# targetFolder = sys.argv[2]

sourceFile = "input/k_stock_200.txt"
targetFolder = r"output"

print os.getcwd()

if not os.path.isfile(sourceFile):
    print "Check Your Input File"
    sys.exit()

output_prefix = "output"
if not os.path.exists(output_prefix):
        os.makedirs(output_prefix)

if not os.path.isdir(targetFolder):
    print "Check Your Output Folder"
    sys.exit()

code_list = getCodeList(sourceFile)

for company_code in code_list:
    iNumber_of_Line = 0
    itooza_url = "http://www.itooza.com/vclub/y10_page.php?cmp_cd=%s&mode=dy&ss=10&sv=1&lsmode=1&accmode=1&lkmode=2"%company_code
    html = urllib.urlopen(itooza_url)
    contents = html.read()

    soup = BeautifulSoup(contents, "lxml")

    if contents.find("id=\"y10_tb_1\"") == -1:
        print "Contunue"
        continue
    
    # Getting Company Name &Code
    h3_tags = soup.find_all("h3")
    for company_info in h3_tags:
        company_name = str(company_info.get_text()).split("\n")[1].strip()
        company_code = str(company_info.find("span").get_text()).strip()

    # Getting Financial Information    
    financail_item_tags = soup.find_all("table", id="y10_tb_1")
    for f_itme in financail_item_tags:
        for y_field in f_itme.find_all("th"):
            financail_items.append(str(y_field.get_text()).strip())
            iNumber_of_Line = iNumber_of_Line + 1

    # print soup.find("table", id="y10_tb_2")

    year_quarter_tags = soup.find("table", id="y10_tb_2").find_all("tr")
    for y_data in year_quarter_tags:
        y_field = y_data.find_all("span")
         
        # Getting Financial Data Period
        for filed_data in y_field:
            if len(str(filed_data.get_text())) > 0:
                year_quarter_items.append(str(filed_data.get_text()).strip())
                
        # Getting Financial Data
        financail_data = y_data.find_all("th", scope="row") 
        if len(financail_data) > 0:
            td_itme = y_data.find_all("td")
            for value in td_itme:
                year_item_data.append(str(value.get_text()).strip())
            
            all_data.append(year_item_data)
            year_item_data = []
            
    # Making output data
    line = "재무상태표"
    for field in year_quarter_items:
        line = line + "\t" + str(field)
    line = line + "\n"
    
    for i in range(0, iNumber_of_Line-1):
        line = line + financail_items[i+1] + "\t"
        for data in all_data[i]:
            line = line + data + "\t"
        line = line + "\n"
        
    file_name = targetFolder +"/" + company_code + "_" + company_name + "_재무재표" + "_" + time.strftime("%Y%m%d") + ".txt"

    # writeFile(file_name.encode("utf-8"), line) # Linux
    writeFile(file_name.encode("cp949"), line) # Windows
    print file_name + " is done!!"
    
    financail_items = []
    year_quarter_items = []
    year_item_data = []
    all_data = []
    time.sleep(5)

