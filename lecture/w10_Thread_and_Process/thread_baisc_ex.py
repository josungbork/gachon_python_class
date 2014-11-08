import threading
from time import ctime

def worker(number):
	for i in range(10):
		print ctime(), number, "Working - ", i,"times"
	return

threads = []

for i in range(5):
	t = threading.Thread(target = worker, args=(i,))
	threads.append(t) 
	t.start()

