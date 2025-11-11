class User:
    pass


attributes = {
        "name":"Sara",
        "email":"sara@example.com",
        "age":27,
        "is_active":True
    }

    
user1 = User()

for key, value in attributes.items():
    setattr(user1, key, value)


for key in attributes:
    print(f"{key}: {getattr(user1, key)}")