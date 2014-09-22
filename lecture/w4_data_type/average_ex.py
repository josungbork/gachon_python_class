kor_score = [49,79,20,100,80]
math_score = [43,59,85,30, 90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score, math_score, eng_score]
student_score = [0,0,0,0,0]
i = 0

for subject in midterm_score:
	for score in subject: 
		student_score[i] += score
		i += 1
	i = 0
else:
	a, b, c, d, e = student_score
	student_average = [a/3.0,b/3.0,c/3.0,d/3.0,e/3.0]
	print student_average, 
