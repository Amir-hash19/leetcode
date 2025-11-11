my_list = [1,2,4,4,9,10,22,1, 25]

def towsum(my_list, target):
    if not my_list:
        return None
    """ this the brute force way to solve this question """
    
    for i in range(len(my_list)):
        f_num = my_list[i]
        for j in range(i-1, len(my_list)):
            s_num = my_list[j]
            if s_num + f_num == target:
                return s_num, f_num
    return None

print(towsum(my_list, 26))