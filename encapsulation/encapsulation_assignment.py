class Encapsulation:
    def __init__(self):
        # one underscore denotes a protected variable
        self._protected = 'a protected variable'
        # two underscores means a private variable that can't be directly
        # accessed outside of the class
        self.__private = 'initial private variable'

    def getPrivate(self):
        print(self.__private)

    def setPrivate(self, private):
        self.__private = private

obj = Encapsulation()

# the protected variable can be accessed as an attribute of the object
print(obj._protected)
obj._protected = 'new protected value'
print(obj._protected)

# the private variable needs methods to be able to access it from inside the object
obj.getPrivate()
obj.setPrivate('this is a new value')
obj.getPrivate()
