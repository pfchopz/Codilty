# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

array = [3, 4, 4, 6, 1, 4, 4]

def solution(N, A):
    # write your code in Python 3.6=
    C = [0] * (N)
    nA = len(A)
    nC = len(C)

    for k in range(nA):
        if A[k] <= N:
            C[A[k] - 1] += 1
        else:
            C = [max(C)] * (N)

    return C

print(solution(5, array))