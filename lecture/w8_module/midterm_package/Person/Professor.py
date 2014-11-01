__author__ = 'blissray'


from Person import Person

class Professor(Person):
    def __init__(self, name, id, midterm):
        Person.__init__(self,name, id)
        self.midterm = midterm

    def getMidTerm(self):
        return self.midterm