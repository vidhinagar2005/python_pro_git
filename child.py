class people:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print("fname = ",self.fname,"\nlname = ",self.lname)

class student(people):
    def __init__(self, fname, lname, address):
        super().__init__(fname,lname)
        self.address = address

s1 = student("vidhi","nagar","odhav")
s1.display()
print("address = ",s1.address)
