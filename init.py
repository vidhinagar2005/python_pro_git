class people:
    def __init__(self, name, address):
        self.name =name
        self.address = address

    def display(self):
        print("name = ",self.name,"\naddress = ",self.address)

s1 = people("vidhi","odhav")
s1.display()