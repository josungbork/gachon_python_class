import random
import sys
from multiprocessing import Process, Queue


class BubbleSortProcess (Process):
	def __init__(self, list):
		Process.__init__(self)
		self.list = list

	def run(self):
		time =0
		for i in range(1,len(self.list)):
			for j in range(1,len(self.list)):
				if self.list[j-1]>self.list[j]: 
					temp = self.list[j]
					self.list[j] = self.list[j-1]
					self.list[j-1] = temp
					time+=1	
		print"The sorted list is as follow:",self.list
		print"The total number of swap is ",time

threads = []

size_of_list=2000

if __name__=='__main__':
	for i in range(5):
		list=range(1,size_of_list+1)
		random.shuffle(list)
		print"The unsorted list is as follow:",list

		p = BubbleSortProcess(list)
		p.start()



