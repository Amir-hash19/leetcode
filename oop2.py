class Person:
    def __init__(self, name, age, salary):
        self.name = name          # عمومی
        self._age = age           # محافظت‌شده
        self.__salary = salary    # خصوصی

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("حقوق باید بیشتر از صفر باشه!")

p = Person("علی", 30, 10000)

# دسترسی مستقیم
print(p.name)      # مجازه
print(p._age)      # می‌شه، ولی توصیه نمی‌شه

# دسترسی به private
# print(p.__salary)  ❌ خطا میده!
print(p.get_salary())  # ✅ روش درست

# تغییر مقدار
p.set_salary(12000)
print(p.get_salary())
