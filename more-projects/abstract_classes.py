from abc import ABC, abstractmethod

# parent class with a regular method and an abstract method
class Parent(ABC):
    def regularMethod(self, num):
        print("Your number is {}".format(num))

    @abstractmethod
    def abstractMethod(self, num):
        pass

# child class that extends the parent and defines the abstract method
class Child(Parent):
    def abstractMethod(self, num):
        print("Your number is {}, this is an abstract method".format(num))


obj = Child()
obj.regularMethod(88)
obj.abstractMethod(34)
