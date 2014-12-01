# -*- coding: utf-8 -*-

print "당신이 태어난 년도를 입력하세요"
byear = int(raw_input())
cyear = 2014
age = cyear - byear + 1
school = ''

if 26 >= age >= 20: school = '대학생'	
elif 20 > age >= 17: school = '고등학생'  	
elif 17 > age >= 14: school = '중학생' 	
elif 14 > age >= 8: school = '초등학생' 	
else: school= '학생이 아니네요' 		
print school
