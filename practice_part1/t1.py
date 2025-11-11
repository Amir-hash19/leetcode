# x = [1,6,4,3,2]
# c = []
# for i in x:
#     if i % 2  == 0:
#         c.append(i)

# print(sum(c))        



# x = "amir"
# l = "".join(reversed(x))
# print(l)


# x = "alireza"

# print(x[::-1])



def find_max():
    x = [4, 12, 7, 3, 15, 9]
    max_num = x[0]  # فرض کن اولین عدد بیشترینه

    for num in x:
        if num > max_num:
            max_num = num  # اگه عدد جدید بزرگ‌تر بود، جایگزینش کن

    return max_num

print(find_max())  # خروجی: 15

            
        