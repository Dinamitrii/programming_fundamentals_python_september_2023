class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car1 = Car("Mercedes", "190 D", 1996)
print(car1.brand)
print(car1.model)
print(car1.year)
print(car1.__dict__)

car1.model = "GLK"
car1.year = 2020

print(car1.brand)
print(car1.model)
print(car1.year)
print(car1.__dict__)
