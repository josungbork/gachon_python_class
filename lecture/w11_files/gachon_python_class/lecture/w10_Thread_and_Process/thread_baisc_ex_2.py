import threading
from time import ctime

class MyThread(threading.Thread):
	def __init__(self, group=None, target=None, name=None, verbose=None, args=()):
		threading.Thread.__init__(self, group=group, target=target, \
			name=name, verbose=verbose)
		self.args=args

	def run(self):
		for i in range(10):
			print ctime(), self.args, "Working - ", i,"times"
		return

for i in range(5):
	t = MyThread(args=(i))
	t.start()

