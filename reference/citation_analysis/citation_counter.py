#!/usr/bin/python

def fileWrite(content, fileName):
	with open(fileName,"w") as f:
		writer = csv.writer (f, delimiter="\t", quotechar ='"')
		for line in content:
			writer.writerow(line)
		f.close()


import MySQLdb
import csv
import sys
  
sourceFile = sys.argv[1]
targetFile = sys.argv[2]

# Open database connection
db = MySQLdb.connect("localhost","root","Piligram2014","citation_db" )
cursor = db.cursor()

file = open(sourceFile) 
AB_patents = csv.reader(file, delimiter='\t', quotechar ='"')
AB_patent_citations = []
citation = []
for line in AB_patents:
	# sql = "select applicationNumber from citation_db.t_document where ApplicationDate like '"+ google_app_date + "%' and ApplicationNumber like '%" +google_app_number +"';"

	# sql = "select ApplicationID  from uspto_patents.PUBLICATIONS where FileDate like '"+ google_app_date +"%' and ApplicationID like '%"+  google_app_number+ "';"
	if len(line[1]) > 0 :
		sql = "select grant_number,grant_kind,cited_number ,cited_kind , category from citation_db.t_citation where grant_number like '%" +line[1] + "' or cited_number like '%"+line[1]+"';"
		print sql
		cursor.execute(sql)
		for (gn, gk, cn, ck, category) in cursor:
			citation.append(gn)
			citation.append(gk)
			citation.append(cn)
			citation.append(ck)
			citation.append(category)
			AB_patent_citations.append(citation)
			citation =[]

		if cursor.rowcount == 0:
			sql = "select GrantId, kind, citedID, kind, category  from uspto_patents.GRACIT_G where grantID like '%"+ line[1]   +"' or citedID like '%"+line[1]  +"';"
			cursor.execute(sql)
			for (gn, gk, cn, ck, category) in cursor:
				citation.append(gn)
				citation.append(gk)
				citation.append(cn)
				citation.append(ck)
				citation.append(category)
				AB_patent_citations.append(citation)
				citation =[]
		print AB_patent_citations
db.close()

fileWrite(AB_patent_citations, targetFile)

