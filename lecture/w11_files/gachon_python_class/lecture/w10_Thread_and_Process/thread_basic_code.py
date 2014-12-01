def worker(number):
	for i in range(10):
		print "=====>", number, "Working - ", i,"times"


for i in range(5):
	worker(i)
