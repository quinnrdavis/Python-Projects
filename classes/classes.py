class Building:
    address = "123 Fake Street"
    squareFeet = 0
    numberOfFloors = 0

class House(Building):
    bedrooms = 0
    bathrooms = 0
    forSale = False

class Store(Building):
    owningBusiness = ""
    openForBusiness = True
