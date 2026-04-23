# Constructor=> It is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the class. The constructor method is defined using the __init__() method.
class Car: #creating a class named Car
    def __init__(self,make,model):
        self.make=make
        self.model=model
c1=Car(2020,"Toyota")
c2=Car(2025,"Deepal")
print(c1.make)
print(c1.model)
print(c2.make)
print(c2.model)