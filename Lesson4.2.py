# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
array = [3, 4, 4, 6, 1, 4, 4]

def solution(N, A):
    # write your code in Python 3.6
    count = [0] * N
    largest = 0


    for i in A:
        if i > N:
            count = [largest] * N
        else:
            count[i - 1] += 1
            if count[i - 1] > largest:
                largest = count[i - 1]

    return count

print(solution(5, array))




#def solution(N, A):
    # write your code in Python 3.6
#    count = [0] * N
#    largest = 0


#    for i in A:
#        if i > N:
#            count = [largest] * N
#        else:
#            count[i - 1] += 1
#            if count[i - 1] > largest:
#                largest = count[i - 1]

#    return count

#print(solution(5, array))





#def idxr(A, m):
#    dict = {}
#    for k in range(1,m+1):
#        dict[k] = 0

#    return dict

#def solution(X, A):
#    n = len(A)
    # index = [-1] * (m + 1)
#    diction = idxr(A, X)
#    totalsum = sum(diction.keys())

#    for k in range(n):
#        if diction[A[k]] == 0:
#            diction[A[k]] = A[k]
#            tmpsum = sum(diction.values())
#            if tmpsum == totalsum:
#                return k
#        else:
#            pass

#    return -1





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


