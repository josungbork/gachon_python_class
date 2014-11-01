__author__ = 'Sungchul Choi'

class Subject:
    def __init__(self, name="", point_of_question=0, number_of_correct_answer=0):
        self.name = name
        self.point_of_question = point_of_question
        self.number_of_correct_answer = number_of_correct_answer


    def setNumberOfCorrectAnswer(self,number):
        self.number_of_correct_answer = int(number)


    def getScore(self):
        return self.number_of_correct_answer * self.point_of_question

