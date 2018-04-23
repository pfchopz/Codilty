# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
array = [2, 3, 1, 4, 6, 8, 7, 5, 7, 9, 1]

def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)

    for k in range(n):
        count[A[k]] += 1

    return count

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    m = 0

    for i in range(n):
        if A[i] > m:
            m = A[i]

    C = counting(A, m)

    for i in range(n):
        if C[i + 1] == 1:
            pass
        else:
            return 0

    return 1

print(solution(array))
