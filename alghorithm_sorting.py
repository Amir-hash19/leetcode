# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n - 1 - i):
#             if arr[j]>arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr


# print(bubble_sort([12,33,2,56,1223,9999,65]))




# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr


# print(selection_sort([64, 25, 12, 22, 11]))





# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr


# print(insertion_sort([12, 11, 13, 5, 6]))





# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]  
#     less = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)


# print(quick_sort([10, 7, 8, 9, 1, 5]))





def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
