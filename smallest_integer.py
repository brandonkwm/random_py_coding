# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    temp_A = [ele for ele in A if ele > 0] #removing all -ve values
    if temp_A == []:
        max_A = 0
        min_A = 0
    else:
        max_A = max(temp_A)
        min_A = min(temp_A)
    temp_list = []  
        
    while min_A < max_A:
        finder = max_A - min_A
        if finder not in temp_A:
            temp_list.append(finder)
        min_A += min_A

    if temp_A == []:
        return 1
    
    if temp_list == []:
        return max_A+1
    else:
        return min(temp_list)

 #note that the code is wrong.... needs to work on an additional logic e.g. [2] so i should return 1 and not 3...
