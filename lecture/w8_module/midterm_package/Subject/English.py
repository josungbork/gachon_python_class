__author__ = 'Sungchul Choi'

from Subject import Subject

class English(Subject):
    def __init__(self, number_of_correct_answer=0):
        Subject.__init__(self, 'ENGLISH', 5, number_of_correct_answer)
