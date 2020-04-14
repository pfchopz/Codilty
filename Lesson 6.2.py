TestArray = [-5, 5, -5, 4]

def solution(A):
    # write your code in Python 3.6
    A.sort()
    if (A[-2] * A[-3]) < (A[0] * A[1]) and A[-1] > 0:
        return A[-1] * A[0] * A[1]
    else:
        return A[-1] * A[-2] * A[-3]

print(solution(TestArray)) 