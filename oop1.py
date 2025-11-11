class Car:
    def __init__(self, brand, model, year, age):
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.age = int(age)

    def info(self):
        return f"The brand is {self.brand} and the model is {self.model} and the year is {self.year}"
    

    def calculate_age(self):
        return f"The age of car is {self.age - self.year}"

car1 = Car('BMW', 'X4', 2018, 2025)

print(car1.info())
print(car1.calculate_age())
print(car1.__dict__)