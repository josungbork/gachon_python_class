import threading

def worker(number):
	"""thread worker function"""
	for i in range(10):
		print "=====>", number, "Working - ", i,"times"
	return

threads = []

for i in range(5):
	worker(i)
