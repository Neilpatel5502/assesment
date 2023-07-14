class Manufacturer:

    # initializer / instance attributes
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.brands = list()

    # method to add brands to a manufacturer object
    def add_brand(self, brand):
        self.brands.append(brand)

    # method to list all brands of a manufacturer
    def get_brands(self):
        return self.brands

class Car:

    # initializer / instance attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # method to print details of the cars
    def get_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


#Create two manufacturers
manufacturer1 = Manufacturer("XYZ", "Ahmedabad")
manufacturer2 = Manufacturer("ABC", "Gandhinagar")


#Add brands to each manufacturer
manufacturer1.add_brand("Toyota")
manufacturer1.add_brand("Nissan")

manufacturer2.add_brand("BMW")
manufacturer2.add_brand("Audi")
manufacturer2.add_brand("Ford")

#Create Cars for manufacturer1
car1 = Car("Toyota", "MK4", 1994)
car2 = Car("Toyota", "Mk5", 2010)
car3 = Car("Nissan", "R34", 2002)

#Create Cars for manufacturer2
car4 = Car("BMW", "X6", 2014)
car5 = Car("Audi", "A4", 2016)
car6 = Car("Audi", "A8", 2020)
car7 = Car("Ford", "Mustang", 2018)

#Print Car deatails
print(f"Cars manufactured by {manufacturer1.name}")
print(car1.get_details())
print(car2.get_details())
print(car3.get_details())

print(f"\nCars manufactured by {manufacturer2.name}")
print(car4.get_details())
print(car5.get_details())
print(car6.get_details())
print(car7.get_details())
