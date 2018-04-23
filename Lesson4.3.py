# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

array = [3, -1, 2, 1, 5]

def counting(A, m):
    n = len(A)
    count = [0] * (m + 2)

    for k in range(n):
        if A[k] <= 0:
            pass
        else:
            count[A[k]] += 1

    return count

def solution(A):
    # write your code in Python 3.6
    if max(A) > 0:
        m = max(A)
    else:
        m = 1
    C = counting(A, m)
    n = len(C)

    for i in range(1, n):
        if C[i] == 0:
            return i

print(solution(array))