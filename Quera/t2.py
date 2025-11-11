# class Person:
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.age = age

#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
    


# p1 = Person("ali", 30)
# print(type(p1))
# print(p1.greet())   



# class Animal:
#     def __init__(self, species: str, name: str):
#         self.species = species
#         self.name = name

#     def speak(self):
#         print("I am an animal.")


#     def __str__(self):
#         return "I am an animal"    
    
#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.species})"



# a1 = Animal("mammal", "Lion")

# print(repr(a1))



# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("I am a dog.")


#     def fetch(self):
#         return ("I can fetch the ball")    
    





# class Vector:
#     def __init__(self, x, y):
#         self.x, self.y = x, y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# print(v1 + v2)      # (4, 6)
# print(v1 == v2)     # False






# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __len__(self):
#         return len(self.items)

#     def __getitem__(self, index):
#         return self.items[index]

# ml = MyList([10, 20, 30])
# print(len(ml))  # 3
# print(ml[1])    # 20


class Math:
    @staticmethod
    def add(x, y):
        return x + y
    

print(Math.add(3, 3))

    
class Person:
    count = 0


    def __init__(self, name):
        self.name = name
        Person.count += 1


    @classmethod
    def get_count(cls):
        return cls.count



p1 = Person("ali")
p2 = Person("sara")
p3 = Person("john")
print(Person.get_count())
        




class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

p = Person(20)
print(p.age)   # 20
p.age = 30
print(p.age)   # 30
