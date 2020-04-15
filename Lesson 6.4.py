A = [10, 2, 5, 1, 8, 20]
B = [10, 50, 5, 1]

def solution(A):
    # write your code in Python 3.6
    A.sort()

    for i in range(2, len(A)):
        if A[i] + A[i - 1] > A[i - 2]:
            if A[i - 1] + A[i - 2] > A[i]:
                if A[i - 2] + A[i] > A[i - 1]:
                    return 1

    return 0

print(solution(A))