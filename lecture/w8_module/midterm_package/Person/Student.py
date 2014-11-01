__author__ = 'blissray'

from Person import Person
from Subject import Math
from Subject import English
from Subject import Korea

class Studnet(Person):

    def __init__(self):
        pass

    def __init__(self, name="", id="", math=Math.Math(), eng=English.English(), kor=Korea.Korea()):
        Person.__init__(self, name, id)
        self.math = math
        self.eng = eng
        self.kor = kor

    def getMath(self):
        return self.math

    def getKorea(self):
        return self.kor

    def getEnglish(self):
        return self.eng

    def getTotalScore(self):
        return self.math.getScore() + self.kor.getScore() + self.eng.getScore()

    def getAverageScore(self):
        return self.getTotalScore()/3

