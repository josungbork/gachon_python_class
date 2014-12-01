#-*- coding: utf-8 *

__author__ = 'Sungchul Choi'

from subject import english
from subject import korea
from subject import math

from person import professor
from person import student
from exam import midterm

def setStudentInformation(myMidterm):
    number_of_students = int(raw_input("입력할 학생수는 몇명입니까? "))
    for i in range(number_of_students):
        print i+1, "번째 학생의 정보를 입력해주세요."
        name = raw_input("이름을 입력해주세요: ")
        student_id = raw_input("학번을 입력해주세요: ")
        myStudent = student.Studnet(name, student_id, math.Math(), english.English(), korea.Korea())
        myMidterm.appendStudent(myStudent)

    print "정보 입력을 완료하였습니다"

def setSubjectScores(myMidterm):

    for student in myMidterm.students:
        print student.getName(), "님의 점수를 입력해 주세요"
        kor_score = raw_input("국어점수를 정답갯수를 입력해 주시기 바랍니다: ")
        math_score = raw_input("수학점수를 정답갯수를 입력해 주시기 바랍니다: ")
        eng_score = raw_input("영어점수를 정답갯수를 입력해 주시기 바랍니다: ")
        student.getKorea().setNumberOfCorrectAnswer(kor_score)
        student.getMath().setNumberOfCorrectAnswer(math_score)
        student.getEnglish().setNumberOfCorrectAnswer(eng_score)
        print student.getName(), "님의 점수입력이 완료되었습니다."

    print "점수 입력이 완료되었습니다"

def showMidtermResult(myMidterm):
    result_menu = '9999'
    while result_menu <> '0':
        print "A. 학생별 점수 출력"
        print "B. 과목별 평균 점수 출력"
        print "0. 이전 화면으로"
        result_menu = (raw_input("메뉴를 선태하세요: ")).upper()

        if result_menu == "A":
            print getBasicFormat(6).format("Name","Kor","Math","Eng","Total","Avg.")
            for student in myMidterm.students:
                print getBasicFormat(6).format( \
                    student.getName(), \
                    str(student.getKorea().getScore()), \
                    str(student.getMath().getScore()),\
                    str(student.getEnglish().getScore()), \
                    str(student.getTotalScore()), \
                    str(student.getAverageScore()))

        elif result_menu == "B":
            print getBasicFormat(4).format("Kor","Math","Eng","Avg.")
            print getBasicFormat(4).format(\
                str(myMidterm.getAverageScore("KOREA")),\
            str(myMidterm.getAverageScore("MATH")), \
            str(myMidterm.getAverageScore("ENGLISH")), \
            str(myMidterm.getTotalAverageScore()))


        elif result_menu == "0":
            pass
        else:
            print "잘못 입력하였습니다. 다시 입력해주시기 바랍니다."

def getBasicFormat(i):
    value = "{:10}"*i
    return value

print "중간고사 성적입력 프로그램입니다."
print "이름과 직번을 입력하세요."
name = raw_input("이름 :")
person_id = raw_input("직번 :")

myMidterm = midterm.Midterm()
myProfessor = professor.Professor(name , person_id, myMidterm)

user_input = "9999"
while user_input != "0":
    print myProfessor.getName(), "선생님"
    print "아래 메뉴 중 실행을 워하는 메뉴를 선택하세요"
    print "1. 학생 입력"
    print "2. 성적 입력"
    print "3. 결과 보기"
    print "0. 종료"

    user_input = raw_input("선택 : ")

    if user_input == "1":
        setStudentInformation(myMidterm)
    elif user_input == "2":
        setSubjectScores(myMidterm)
    elif user_input == "3":
        showMidtermResult(myMidterm)
    elif user_input == "0":
        continue
    else:
        print "잘못 입력하셨습니다. 다시 입력해 주십시요."
