import threading
from time import ctime

class MyThread(threading.Thread):
	def __init__(self, group=None, target=None, name=None, args=(), verbose=None):
		threading.Thread.__init__(self, group=group, target=target, \
			name=name, verbose=verbose)
		self.args=args

	def run(self):
		"""thread worker function"""
		for i in range(10):
			print ctime(), self.args, "Working - ", i,"times"
		return

threads = []

for i in range(5):
	t = MyThread(args=(i))
	t.start()

