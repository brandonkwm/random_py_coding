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

    i = 1
    while min_A <= max_A:
        test_A = min_A + i
        if test_A not in A:
            return test_A
        i += 1
