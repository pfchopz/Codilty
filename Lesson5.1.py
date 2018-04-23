# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")



def solution(A, B, K):
    # write your code in Python 3.6
    upper = B // K
    lower = (A - 1) // K

    result = upper - lower

    return result


print(solution(6, 11, 2))