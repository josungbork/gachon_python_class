def getCharHexNumber(remain):
	if remain==10:
		return "A"
	if remain==11:
		return "B"
	if remain==12:
		return "C"
	if remain==13:
		return "D"
	if remain==14:
		return "E"
	if remain==15:
		return "F"


def hex(decimal):
	value = decimal
	result = ''
	while(value>0):
		remain = value%16
		value = value//16

		if (remain >= 10 and ramain <=15):
			remain = getCharHexNumber(remain)

		result = str(remain) + result

	return result

	
value = 160

print hex(value)