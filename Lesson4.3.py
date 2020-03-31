# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

array = [-10, -8, -8000, -3, -1, -2, -1, -5]

def solution(A):
    # write your code in Python 3.6
    B = set()
    x = 1

    for i in A:
        if i > 0:
            B.add(i)
    B = sorted(B)

    for i in B:
        if i == x:
            x += 1
        else:
            return x
    return x

print(solution(array))





#def counting(A, m):
#    n = len(A)
#    count = [0] * (m + 2)

 #   for k in range(n):
 #       if A[k] <= 0:
 #           pass
 #       else:
 #           count[A[k]] += 1

 #    return count

#def solution(A):
    # write your code in Python 3.6
#    if max(A) > 0:
#        m = max(A)
#    else:
#        m = 1
#    C = counting(A, m)
#    n = len(C)

#    for i in range(1, n):
#        if C[i] == 0:
#            return i

