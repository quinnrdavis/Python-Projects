from abc import ABC, abstractmethod

class Parent(ABC):
    def regularMethod(self, num):
        print("Your number is {}".format(num))

    @abstractmethod
    def abstractMethod(self, num):
        pass

class Child(Parent):
    def abstractMethod(self, num):
        print("Your number is {}, this is an abstract method".format(num))


obj = Child()
obj.regularMethod(88)
obj.abstractMethod(34)
