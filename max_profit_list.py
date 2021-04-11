def solution(A):
    # write your code in Python 3.6
    begin_index = 0
    end_index = len(A) -1
    profit_list = []
    max_list = []
    i=0
    y=i+1
    while i <len(A):
        while y < len(A):
            profit_list.append(A[y] - A[i])
            max_list.append(max(profit_list))
            y += 1
        i += 1
        y = i+1 #resetting internal loop counter
    
    return max(max_list)

A = [23171, 21011, 21123, 21366, 21013, 21367]
solution(A)
