array = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
next = [1, 1, 3, 3, 5, 5, 10, 10, 10, 10, 10, -1]

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    peaks = []

    for i in range(1, N):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)



    print(peaks)
print(solution(array))