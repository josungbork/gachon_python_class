my_file = open("i_have_a_dream.txt", "r")

contents = my_file.read() 
print type(contents), contents 

my_file.seek(0) 
content_list = my_file.readlines() 
print type(content_list), content_list 

i = 0
my_file.seek(0) 
while 1: 
    line = my_file.readline() 
    if not line: break 
    print "line:",str(i) + " === " + line
    i = i + 1
