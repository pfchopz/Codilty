# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

array = [3, 1, 2, 4, 3]

def solution(A):
    # write your code in Python 3.6
    d = 2002
    n = 0
    s = sum(A)

    for i in range(len(A) - 1):
        n += A[i]
        f = s - n
        a = abs(n - f)
        if a < d:
            d = a

    return d

print(solution(array))