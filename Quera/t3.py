def find_max(num_list):
    default_max = num_list[0]
    for num in num_list:
        if num > default_max:
            default_max = num
    return default_max        

# my_list = [99,4,5, 12,22, 44,]

# print(find_max(my_list))




def sum(num_list):
    result = 0
    for i in range(len(num_list)):
        result += num_list[i] 
    return result

# print(sum([5,4,1,22]))    






# for i in range(1,11):
#     print(i)



# result = 0
# for num in range(1, 101):
#     result += num
# print(result)    


# for num in [19,11,7,3]:
#     print(num)




# def find_max_sum(num_list) -> int:
#     max_default = num_list[0]
#     total = 0

#     for num in num_list:
#         total += num
#         if num > max_default:
#             max_default = num 

#     return f"the sum of the listnumber is {total} and the max number is {max_default}"

# print(find_max_sum([4,1,7,100]))


# def sum_even(my_list) ->int:
#     list_num = [i for i in my_list if i % 2==0]
#     return sum(list_num)

# print(sum_even([2,3,4,5,6]))



# def square(x):
#     return x**2

# print(square(5))



# square_lambda = lambda x: x**2
# print(square_lambda(5))





# numbers = [1,2,3,4,5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)




# nubmers = [1,2,3,4,5,6]
# even_number = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_number)




# numbers = [1,2,3,4,5,6]

# result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# print(result)




# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)




# def revese_func(word:str) -> str:
#     return word == word[::-1]

# print(revese_func("1111"))