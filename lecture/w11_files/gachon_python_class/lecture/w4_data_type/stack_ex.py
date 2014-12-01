user_input = raw_input()
stack = []

for char in user_input:
	stack.append(char)
print len(stack)

while len(stack)>0:
	print stack.pop(0),

