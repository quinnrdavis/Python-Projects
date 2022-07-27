class Cat:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def info(self):
        msg = "\n{} is a {} cat".format(self.name, self.species)
        return msg






if __name__ == "__main__":
    cat = Cat("Blackberry", "Black Shorthair")
    print(cat.info())
