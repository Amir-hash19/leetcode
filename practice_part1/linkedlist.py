# x = [i for i in range(100) if i % 2 ==0]
# print(x[  ::-1 ])
# [1, 2, 3, 4, 5 ,6]


# def reverse_array(arr):
#     left = 0
#     right = len(arr) - 1
#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1
#     return arr


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):  # ← تابع اضافه به ابتدای لیست
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



def count_nodes(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count




class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)




def is_balanced(string):
    stack = []
    opening = "([{"
    closing = ")]}"
    match = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()

    return len(stack) == 0



def reverse_string(s):
    stack = []
    
    # همه کاراکترها رو push کن
    for char in s:
        stack.append(char)
    
    reversed_str = ""
    
    # تا زمانی که stack خالی نیست، pop کن و به رشته اضافه کن
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str





class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # اضافه به انتها

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)  # حذف از ابتدای لیست

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
