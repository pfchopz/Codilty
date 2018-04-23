# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

TestArray = [0,1,2,3,4,5,6,7,8,9]

def solution(A, K):
    # write your code in Python 3.6
    for j in range(K):
        for idx, value in enumerate(A):
            A[idx], A[0] = A[0], A[idx]

    return A

print(solution(TestArray, 7))