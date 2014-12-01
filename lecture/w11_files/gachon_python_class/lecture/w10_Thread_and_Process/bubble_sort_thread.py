import random
import sys
import threading


def swap_reference (sort_list):
	time =0
	for i in range(1,len(sort_list)):
		for j in range(1,len(sort_list)):
			if sort_list[j-1]>sort_list[j]: 
				temp = sort_list[j]
				sort_list[j] = sort_list[j-1]
				sort_list[j-1] = temp
				time+=1
	
	print"The sorted list is as follow:",sort_list
	print"The total number of swap is ",time

threads = []

size_of_list=2000

for i in range(5):
	list=range(1,size_of_list+1)
	random.shuffle(list)
	print"The unsorted list is as follow:",list
	t = threading.Thread(target = swap_reference, args=(list,))
	t.start()



