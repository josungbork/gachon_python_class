__author__ = 'Sungchul Choi'

from subject import Subject

class Korea(Subject):

    def __init__(self, number_of_correct_answer=0):
        Subject.__init__(self, 'KOREA', 4, number_of_correct_answer)