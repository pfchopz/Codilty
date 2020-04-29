array = [3, 2, -6, 4, 0]

def solution(A):
    # write your code in Python 3.6
    max_ending = max_slice = 0
    largestNum = max(A)
    if largestNum < 0:
        max_slice = largestNum
    else:
        for i in A:
            max_ending = max(0, max_ending + i)
            max_slice = max(max_slice, max_ending)
    return max_slice

print(solution(array))