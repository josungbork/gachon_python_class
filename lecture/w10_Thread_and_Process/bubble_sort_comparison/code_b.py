import random
import sys

def swap_reference (sort_list,offset_x,offset_y):
	temp = sort_list[offset_x]
	sort_list[offset_x] = sort_list[offset_y]
	sort_list[offset_y] = temp

size_of_list=5000
unsorted_list=[]

list=range(1,size_of_list+1)
random.shuffle(list)
print"The unsorted list is as follow:",list

time=0

for i in range(1,len(list)):
	for j in range(1,len(list)):
		if list[j-1]>list[j]: 
			swap_reference(list,j-1,j)
			time+=1

print" "
print"The sorted list is as follow:",list
print"The total number of swap is ",time
print" "			 
