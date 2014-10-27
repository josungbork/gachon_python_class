def swap_value (x, y):
	temp = x
	x = y
	y = temp

def swap_offset (offset_x, offset_y):
	temp = a[offset_x]
	a[offset_x] = a[offset_y]
	a[offset_y] = temp

def swap_reference (list, offset_x, offset_y):
	temp = list[offset_x]
	list[offset_x] = list[offset_y]
	list[offset_y] = temp

a = [1,2,3,4,5]
swap_value(a[1], a[2])
print a
swap_offset(1,2)
print a
swap_reference(a, 1, 2)
print a

