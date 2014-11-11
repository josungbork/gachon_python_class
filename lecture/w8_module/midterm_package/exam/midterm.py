__author__ = 'blissray'


class Midterm:
    def __init__(self):
        self.students = []

    def appendStudent(self, student):
        self.students.append(student)

    def findStudentByName(self, name):
        for student in self.students:
            if (student.getName() == name):
                return student
        return "0"

    def findStudentByID(self, id):
        for student in self.students:
            if (student.getID() == id):
                return student
        return "0"

    def getAverageScore(self, subject_name):
        sum = 0
        for studnet in self.students:
            sum += self.getScoreOfSubject(studnet, subject_name)

        return sum / len(self.students)

    def getTotalAverageScore(self):
        return (self.getAverageScore("MATH") + self.getAverageScore("ENGLISH") + self.getAverageScore("KOREA"))/3

    def getScoreOfSubject (self, student, subject_name):
        if subject_name.upper() == "MATH":
            return student.getMath().getScore()

        if subject_name.upper() == "ENGLISH":
            return student.getEnglish().getScore()

        if subject_name.upper() == "KOREA":
            return student.getKorea().getScore()


