import math

def getValuesOfQuadraticEquation(a, b, c):
	values = []
	values.append((-b + math.sqrt(b ** 2 - (4 * a * c)) )  / (2 * a))
	values.append((-b - math.sqrt(b ** 2 - (4 * a * c)) )  / (2 * a))
	return values

print getValuesOfQuadraticEquation(1,-2,1) 