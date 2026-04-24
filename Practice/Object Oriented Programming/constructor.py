# Constructor=> It is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the class. The constructor method is defined using the __init__() method.
class Car: #creating a class named Car
    def __init__(self,make,model): #creating a constructor method that takes two parameters make and model
        self.make=make #self is a reference to the current instance of the class, and it is used to access the attributes and methods of the class. Here we are initializing the make attribute with the value passed as an argument to the constructor.
        self.model=model
c1=Car(2020,"Toyota") 
c2=Car(2025,"Deepal")
c3=Car(2023,"Honda")
print(c1.make)
print(c1.model)
print(c2.make)
print(c2.model)
print(c3.make)
print(c3.model)