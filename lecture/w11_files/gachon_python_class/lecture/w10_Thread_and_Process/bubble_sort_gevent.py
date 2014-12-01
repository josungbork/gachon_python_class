import random
from gevent import monkey
from gevent.pool import Pool

def swap (sort_list):
	time =0
	for i in range(1,len(sort_list)):
		for j in range(1,len(sort_list)):
			if sort_list[j-1]>sort_list[j]: 
				temp = sort_list[j]
				sort_list[j] = sort_list[j-1]
				sort_list[j-1] = temp
				time+=1
	
	print"The sorted list is as follow:"
	print"The total number of swap is ",time

monkey.patch_all()
pool = Pool(3)

number_of_loop = range(100)
for i in number_of_loop:
	size_of_list=1000
	list=range(1,size_of_list+1)
	random.shuffle(list)
	print"The unsorted list is as follow:"
	pool.spawn(swap, list)
	

