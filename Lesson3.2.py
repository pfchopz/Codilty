# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

array = [2, 3, 1, 4, 6, 7]

def solution(A):
    # write your code in Python 3.6
    l = len(A)
    s = sum(A)
    S = ( (l + 1) * (l + 2) ) / 2
    a = int(S - s)

    return a

print(solution(array))