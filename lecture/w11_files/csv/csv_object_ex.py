 #-*- coding: utf-8 -*- 

import csv

seoung_nam_data = []
header = []
rownum = 0

with open("korea_floating_population_data.csv","r") as p_file:
	csv_data = csv.reader(p_file)
	for row in csv_data:
		if rownum == 0: header = row
		location = row[7].decode("cp949")
		if location.find(u"성남시") != -1: seoung_nam_data.append(row)
		rownum +=1

with open("seoung_nam_floating_population_data.csv","w") as s_p_file:
	writer = csv.writer(s_p_file, delimiter=',', \
		quotechar="'", quoting=csv.QUOTE_ALL)
	writer.writerow(header)
	for row in seoung_nam_data: writer.writerow(row)