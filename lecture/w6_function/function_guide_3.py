def isUniversityStudent(birthday):
	return True if birthday <= 1992 else False

def isHighSchoolStudent(birthday):
	return True if (birthday > 1992 and birthday < 1996): else False

def isMiddleSchoolStudent(birthday):
	return True if (birthday > 1996 and birthday < 2000) else False


birthday = 1992
if (isUniversityStudent(birthday)):
	print "Hello! University Student"

if isHighSchoolStudent(birthday):
	print "Hello! High School Student"

if isMiddleSchoolStudent(birthday):
	print "Hello! Middle Student"
