# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
array = [2, 3, 1, 4, 6, 8, 7, 5, 10, 9, 10, 8]


def idxr(A, m):
    dict = {}
    for k in range(1,m+1):
        dict[k] = 0

    return dict

def solution(X, A):
    n = len(A)
    # index = [-1] * (m + 1)
    diction = idxr(A, X)
    totalsum = sum(diction.keys())

    for k in range(n):
        if diction[A[k]] == 0:
            diction[A[k]] = A[k]
            tmpsum = sum(diction.values())
            if tmpsum == totalsum:
                return k
        else:
            pass

    return -1

# def solution(X, A):
#     C = indexer(A, X)
#     # C = idxr(A, X)
#     n = len(C)
#     index = 0
#
#     for i in range(1, n):
#         if C[i] == -1:
#             return -1
#         else:
#             pass
#
#     for j in range(n):
#         if C[j] > index:
#             index = C[j]
#
#     return index


print(solution(10, array))