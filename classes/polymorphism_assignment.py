# general plant class with some default values
class Plant:
    color = "Green"
    environment = ""
    height = 0

    # .grow() method, by default plants grow a small amount
    def grow(self):
        self.height += 1

class Tree(Plant):
    color = "Green"
    environment = "Forest"
    height = 0

    # trees on average grow a lot taller than other plants
    def grow(self):
        self.height += 10

class Potato(Plant):
    color = "Brown"
    environment = "Underground"
    # height does not matter for potatoes so instead they have a diameter attribute
    diameter = 0

    # potatoes do not grow taller because they grow underground, instead they grow larger
    def grow(self):
        self.diameter += 1
