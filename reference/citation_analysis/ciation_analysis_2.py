#!/usr/bin/python

def fileWrite(content):
	with open("modified_qd_citation.csv","w") as f:
		writer = csv.writer (f, delimiter="\t", quotechar ='"')
		for line in content:
			writer.writerow(line)
		f.close()


import MySQLdb
import csv

# Open database connection
db = MySQLdb.connect("localhost","root","Piligram2014","citation_db" )
cursor = db.cursor()
# cursor.execute("SELECT * from t_document")
# data = cursor.fetchone()

file = open('qd_csv.csv') 
AB_patents = csv.reader(file, delimiter='\t', quotechar ='"')
AB_patent_info = []
info = []
for line in AB_patents:
	wips_application = line[0]
	wips_grant = line[1]
	application = line[0].split("-")
	google_app_number = application[1]
	google_app_date = application[0]

	if wips_grant != '':
		google_grant = str(0) + wips_grant
	else:
		google_grant = ''

	patent_assignee = line[2]
	assignee_country = line[3]
	info.append(wips_application)
	info.append(wips_grant)
  	
	# sql = "select applicationNumber from citation_db.t_document where ApplicationDate like '"+ google_app_date + "%' and ApplicationNumber like '%" +google_app_number +"';"

	sql = "select ApplicationID  from uspto_patents.PUBLICATIONS where FileDate like '"+ google_app_date +"%' and ApplicationID like '%"+  google_app_number+ "';"

	cursor.execute(sql)
	data = cursor.fetchone()

	if data is not None:
		print data[0]
		info.append(data[0])
	else:
		info.append(" ")

	info.append(google_grant)
	info.append(patent_assignee)
	info.append(assignee_country)
	AB_patent_info.append(info)	
	info = []	
db.close()
fileWrite(AB_patent_info)

