class Person:
    def __init__(self, name, age:int):
        self.name = name
        self.age = age


    def say_hello(self):
        return(f"hi my name is {self.name} and i am {self.age}") 
    




class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color


    def drive(self):
        print(f"{self.model} is ready to drive !")





class BackAccount:
    def __init__(self, balance:int):
        self.__balance = balance


    def deposit(self, amount:int):
        self.__balance += amount



    def get_balance(self):
        print(f"Your balance is {self.__balance}")

    def take_money(self, amount:int):
        return f"your ccurrent balance is -> {self.__balance - amount}"    






class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(3, 5))  # 8





import functools

@functools.lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(35))  # سریع‌تر اجرا میشه به خاطر کش شدن نتایج






def my_decorator(func):
    def wrapper():
        print("قبل از اجرا")
        func()
        print("بعد از اجرا")
    return wrapper

@my_decorator
def say_hi():
    print("سلام!")

say_hi()







class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.cpu = self.CPU()

    class CPU:
        def info(self):
            return "Intel i7"

c = Computer("Dell")
print(c.brand)
print(c.cpu.info())





class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"کلاسی به نام {name} ساخته شد")
        return super().__new__(cls, name, bases, dct)

class Person(metaclass=Meta):
    def __init__(self, name):
        self.name = name
