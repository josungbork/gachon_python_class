#!/usr/bin/python
# -*- coding: utf-8 -*-

print "총 학생 수는 몇명입니까?",
number_of_student = int(raw_input())

print "총 과목은 몇과목 입니까?",
number_of_subject = int(raw_input())

student_list = []
for i in range(number_of_student):
	print i+1,"번째 학생의 이름을 넣어주세요: ",
	student_list.append(raw_input())
print "학생 이름 입력이 완료되었습니다. \n\n"

subject_list = []
for i in range(number_of_subject):
	print i+1,"번째 과목의 이름을 넣어주세요: ",
	subject_list.append(raw_input())
print "과목 이름 입력이 완료되었습니다. \n\n"

score_matrix= []
student_score = [] 
for student in student_list:
	for subject in subject_list:
		print student, "학생의", subject,"점수를 입력하세요: ",
		subject_score = float(raw_input())
		student_score.append(subject_score)

	print student, "학생의 점수 입력이 완료되었습니다\n\n"
	score_matrix.append(student_score)
	student_score = []

selected_menu = -1
while selected_menu <> 0:
	print "1. 과목별 점수 조회"
	print "2. 학생별 점수 조회"
	print "0. 프로그램 종료\n"
	print "원하는 메뉴를 입력하세요: ",

	selected_menu = int(raw_input())

	if selected_menu == 1:
		subject_selected_menu = - 1

		while subject_selected_menu <> 0:
			for i in range(len(subject_list)):
				print i+1, "-", subject_list[i]
			print "점수를 보고 싶은 과목을 선택하세요(0 - 이전메뉴)",

			subject_selected_menu = int(raw_input())
			if subject_selected_menu == 0:
				break
			elif subject_selected_menu <= len(subject_list):
				student_number = 0
				for score in score_matrix:
					print student_list[student_number], "의 점수는",
					print score[subject_selected_menu-1]
					student_number = student_number + 1
			else:
				print "다시 입력해 주시기 바랍니다"

	elif selected_menu== 2:
		student_selected_menu = - 1
		while student_selected_menu <> 0:
			for i in range(len(student_list)):
				print i+1, "-", student_list[i]
			print "점수를 보고 싶은 학생을 선택하세요(0 - 이전메뉴)",

			student_selected_menu = int(raw_input())
			if student_selected_menu == 0:
				break
			elif student_selected_menu <= len(student_list):
				subject_number = 0
				for score in score_matrix[student_selected_menu-1]:
					print subject_list[subject_number], "점수:",score
					subject_number = subject_number + 1
			else:
				print "다시 입력해 주시기 바랍니다"


	elif selected_menu == 0:
		print "프로그램을 종료합니다. 감사합니다."
		break
	else:
		print "잘못 입력하셨습니다. 다시 입력해주시기 바랍니다 \n"



