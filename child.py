class people:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print("fname = ",self.fname,"\nlname = ",self.lname)

class student(people):
    pass

s1 = student("vidhi","nagar")
s1.display()