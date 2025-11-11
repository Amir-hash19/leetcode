# my_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

# x = list(str(input()))
my_list = list(str(input()))
def test(my_list):
    for i in range(len(my_list)):
        if my_list[i] == "I":
            my_list[i] = 1
        elif my_list[i] == "V":
            my_list[i] = 5
        elif my_list[i] == "X":  
            my_list[i] = 10  
        elif my_list[i] == "L":    
            my_list[i] = 50
        elif my_list[i] == "C":    
            my_list[i] = 100
        elif my_list[i] == "D":    
            my_list[i] = 500 
        elif my_list[i] == "M":    
            my_list[i] = 1000
    return sum(my_list)    
print(test(my_list))


    
    
    
        
    
           
    
        

           
         














    
















# for num in range(len(x)):
#     if I in x:
#         I = 1
#         result.append(I)
#     elif V in x:
#         V = 5
#     elif X in x:
#         X = 10
#     elif L in x:
#         L = 50
#     elif C in x:
#         C = 100
#     elif D in x:
#         D = 500
#     elif M in x:
#         M = 1000                           

# print(x)

    