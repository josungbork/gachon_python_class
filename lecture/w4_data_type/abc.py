import random

c_flag = True 

while c_flag == True:
	r_number = str(random.randint(100,999))

	if (r_number[0] == r_number[1] or r_number[1] == r_number[2] or r_number[0] == r_number[2]):
		print "Test :", r_number
		r_number = str(random.randint(100,999))
		c_flag = True
	else:
		c_flag = False

print r_number
