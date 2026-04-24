class Person:
    def __init__(self, name):
        self.name=name
    def show(self): # show is a method that prints the name of the person. It uses the self parameter to access the name attribute of the class.
        print(self.name)
p=Person("Hari")
p.show()