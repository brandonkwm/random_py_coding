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
    
    #binary search to reduce the upper limit for faster performance
    mid_val = (max_A + min_A) // 2 #get floor of value
    while mid_val < max_A:
        if mid_val not in A & mid_val < max_A & mid_val > min_A:
            max_A = mid_val-1
        else:
            max_A = mid_val+1
        mid_val = (max_A + min_A) // 2 


    i = 1
    if min(temp_A) > 2:
        while i < max_A:
            test = min_A + i
            if test not in A:
                return test
            i += 1
    elseif min(temp_A) == 2:
        return 1

