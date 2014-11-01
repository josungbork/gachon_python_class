__author__ = 'Sungchul Choi'

from Subject import Subject

class Math(Subject):
    def __init__(self, number_of_correct_answer=0):
        Subject.__init__(self, 'MATH', 3, number_of_correct_answer)


