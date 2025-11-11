class User:
    pass


user1 = User()


setattr(user1, "name", "ali")
setattr(user1, "email", "test@example.com")
setattr(user1, "age", 30)

print(getattr(user1, "name"))
print(getattr(user1, "email"))
print(getattr(user1, "age"))