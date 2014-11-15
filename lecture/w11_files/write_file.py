import os

with open("file_name_list.txt","w") as f:
	for curdir, dirs, files in os.walk('./gachon_python_class'):
		f.write("Current Directory :" + curdir + "\n")

		if len(dirs):
			f.write("Directory List" + "\n")
			dirlist = ""
			for dir in dirs:
				dirlist = dirlist + dir + "\t" + str(len(files)) + "\n"
			f.write(dirlist+"\n")

		if len(files):
			f.write("File List List" + "\n")
			filelist = ""
			for file in files:
				filelist = filelist + file + "\t" + str(os.path.getsize (curdir+"/"+file))+"KB" + "\n"
			f.write(filelist+"\n")

		f.write(("-"*60)+"\n")
