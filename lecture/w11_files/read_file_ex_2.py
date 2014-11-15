my_file = open("i_have_a_dream.txt", "r")

contents = my_file.read() 
word_list = contents.split(" ")
line_list = contents.split("\n")

print "Total Number of Characters :", len(contents)
print "Total Number of Words:", len(word_list)
print "Total Number of Lines :", len(line_list) 
