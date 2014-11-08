import random

def swap(A,x,y):
	temp=A[x]
	A[x]=A[y]
	A[y]=temp

def sort(randomlist):
	global number
	number=0
	for i in range(len(randomlist)-1):
		for j in range(1,len(randomlist)-i):
			if randomlist[j-1]>randomlist[j]:
				swap(randomlist,j-1,j)
				number+=1
	print randomlist

randomlist=[]

size = 2000
print "The unsorted list is as follows:"

for i in range(5):
	listsize=range(1,size+1)
	randomlist=random.sample(listsize,size)

	print randomlist
	print""
	print"The sorted list is as follows:"

	after=sort(randomlist)
	print"The total number off swap is",number
	print""
