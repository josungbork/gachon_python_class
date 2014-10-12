decimal = 10
result = '' 
while (decimal > 0):
	decimal = decimal / 2
	remainder = decimal % 2
	result = result + str(remainder)
print result

