from multiprocessing import Process, Queue
import time 
def worker(number):
	"""thread worker function"""
	for i in range(10):
		print time.ctime(), number, "Working - ", i,"times"
	return

if __name__=='__main__':
	threads = []
	for i in range(5):
		t = Process(target = worker, args=(i,))
		t.start()
	
