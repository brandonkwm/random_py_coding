# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    temp_A = [ele for ele in A if ele > 0] #removing all -ve values
    if temp_A == []:
        max_A = 0
        min_A = 0
        median_A = 0
    else:
        max_A = max(temp_A)
        min_A = min(temp_A)
        median_A = temp_A[len(temp_A)//2]
    
    #bring max val closer to median to limit search for better perf
    mid_val = (max_A + min_A) // 2 #get floor of value
    while mid_val < max_A and mid_val > median_A:
        if mid_val not in temp_A: 
            max_A = mid_val
        mid_val = (max_A + mid_val) // 2 

    mid_val = (min_A + median_A) // 2 #get floor of value
    while mid_val < max_A and mid_val < median_A and mid_val > min(temp_A):
        if mid_val not in temp_A: 
            min_A = mid_val
        mid_val = (min_A + mid_val) // 2 


    i = 1
    if max_A == 0:
        return 1
    elif min(temp_A) != 2:
        while i <= max_A:
            test = min_A + i
            if test not in A:
                return test
            i += 1
    elif min(temp_A) == 2:
        return 1


