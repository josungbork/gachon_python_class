# -*- coding: utf-8 -*-

class Person:	# 부모 클래스 Person 선언
	def __init__(self, name, age, gender):
		self.name = name # 속성값 지정, 해당 변수가 클래스의 attribute임을 명확히하기 위해 self를 붙임
		self.age = age
		self.gender = gender
	def aboutMe(self): # 메서드 선언
		print "저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다."

class Employee(Person):	 # 부모 클래스 Person으로 부터 상속
	def __init__(self, name, age, gender, salary, hiredate):
		Person.__init__(self, name, age, gender) # 부모객체 사용
		self.salary = salary
		self.hiredate = hiredate	 # 속성값 추가
	def doWork(self):	 # 새로운 메서드 추가
		print("열심히 일을 합니다.")
	def aboutMe(self):	 # 부모 클래스 메서드 재정의
		Person.aboutMe(self)
		print "제 급여는 ", self.salary, "원 이구요, 제 입사일은 ", self.hiredate , " 입니다."


myPerson = Person("John", 34, "Male")
myEmployee = Employee("Daeho", 34, "Male", 300000, "2012/03/01")
myPerson.aboutMe()
myEmployee.aboutMe()