Array = [4, 2, 2, 5, 1, 5, 8]


def solution(A):
    # write your code in Python 3.6
    minAvg = (A[0] + A[1]) / 2
    sliceLoc = 0

    for i in range(len(A) - 2):

        if (A[i + 1] + A[i]) / 2 < minAvg:
            minAvg = (A[i + 1] + A[i]) / 2
            sliceLoc = i

        if (A[i + 2] + A[i + 1] + A[i]) / 3 < minAvg:
            minAvg = (A[i + 2] + A[i + 1] + A[i]) / 3
            sliceLoc = i

    if (A[-1] + A[-2]) / 2 < minAvg:
        minAvg = (A[-1] + A[-2]) / 2
        sliceLoc = len(A) - 2

    return sliceLoc


print(solution(Array))