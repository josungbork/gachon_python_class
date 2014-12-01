import os

# print "Output : ", os.listdir("./gachon_python_class")

# #os.walk(top,topdown=True, oneerror=None,followlinks=False)
# #Return Info: dirpath, dirnames, filenames
# for curdir, dirs, files in os.walk('./gachon_python_class'):
# 	print "Current Directory :", curdir
# 	print "Directory List :", dirs
# 	print "File List :", files
# 	print

root_dir = "./gachon_python_class/lecture/w8_module/midterm_package"
file_list = os.listdir(root_dir)
print type(file_list)

for file in file_list:
	print "File Name -", file,
	if os.path.isfile(root_dir+"/"+file): print "is File"
	if os.path.isdir(root_dir+"/"+file): print "is Directory"