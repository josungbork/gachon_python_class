# -*- coding: utf-8 -*-

print "구구단 몇단을 계산할까요?"
x = int(raw_input())
print "구구단 " + str(x) +"단을 계산합니다."
for i in range(1,10):
	print str(x) + " X " + str(i) + " = " + str(x*i)
