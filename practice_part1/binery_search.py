# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1


#     while low <= high:
#         mid = (low + high) // 2
#         guess = list[mid]

#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1
        
# print(binary_search([-1, 0, 3, 4, 9, 9,12], 12))


# def binary_search(nums, target):
#     def find_first(nums, target):
#         low, high = 0, len(nums) - 1
#         index = -1
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] == target:
#                 index = mid
#                 high = mid - 1  # ادامه جستجو سمت چپ
#             elif nums[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return index

#     def find_last(nums, target):
#         low, high = 0, len(nums) - 1
#         index = -1
#         while low <= high:
#             mid = (low + high) // 2
#             if nums[mid] == target:
#                 index = mid
#                 low = mid + 1  # ادامه جستجو سمت راست
#             elif nums[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return index

#     return [find_first(nums, target), find_last(nums, target)]

# print(binary_search([-1, 0, 3, 4, 9, 9,12], 9))



def average_even(my_list):
    evens = [i for i in my_list if i % 2 == 0]
    
    if not evens:
        return 0  # یا مثلاً: raise ValueError("No even numbers")
    
    return sum(evens) / len(evens)

print(average_even([12, 3, 12, 33]))  # خروجی: 12.0









