import requests
import csv

url = 'http://real-chart.finance.yahoo.com/table.csv?s=005930.KS&a=0&b=1&c=2013&d=11&e=31&f=2014&g=d'

r = requests.get(url)
day_data = []
header = []
stock_data = []
linecounter = 0
for line in r.content.split("\n"):
	if linecounter == 0:
		header = line.split(",")
	else:
		if len(line) != 0:
			day_data = line.split(",")
			stock_data.append(day_data)
	linecounter += 1

month_average = []
yealy_report = []

open_initial = 0.0
high_initial = 0.0
low_initial = 0.0
close_initial = 0.0
volume_initial = 0.0
adj_close_initial = 0.0
number_of_days = 0.0

current_month = ''
for day_data in stock_data:
	if current_month == day_data[0].split("-")[1]:

		open_initial += float(day_data[1])
		high_initial += float(day_data[2])
		low_initial += float(day_data[3])
		close_initial += float(day_data[4])
		volume_initial += float(day_data[5])
		adj_close_initial += float(day_data[6])
		number_of_days += 1




	else:

		if number_of_days != 0:
			month_average.append(day_data[0].split("-")[0] + "-" + day_data[0].split("-")[1])

			month_average.append(open_initial /number_of_days)
			month_average.append(high_initial /number_of_days)
			month_average.append(low_initial /number_of_days)
			month_average.append(close_initial /number_of_days)
			month_average.append(volume_initial /number_of_days)
			month_average.append(adj_close_initial /number_of_days)
			yealy_report.append(month_average)
			month_average =[]

			open_initial = float(day_data[1])
			high_initial = float(day_data[2])
			low_initial = float(day_data[3])
			close_initial = float(day_data[4])
			volume_initial = float(day_data[5])
			adj_close_initial = float(day_data[6])

			number_of_days = 1

	current_month = day_data[0].split("-")[1] 

with open('samsung.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL, )
    writer.writerow(header)
    
    for row in yealy_report:
		writer.writerow(row)
    