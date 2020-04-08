Array = [0, 1, 0, 1, 1]

def solution(A):
    # write your code in Python 3.6
    zeroCount = 0
    totalPairs = 0

    for i in A:
        if i == 0:
            zeroCount += 1
        else:
            totalPairs += (1 * zeroCount)

    if totalPairs > 1000000000:
        totalPairs = -1

    return totalPairs

print(solution(Array))



#With PrefixSums
#def solution(A):
    # write your code in Python 3.6
#    totalPairs = 0
#    prefixSum = [A[0]] * len(A)

#    for i in range(1, len(A)):
#        prefixSum[i] = prefixSum[i - 1] + A[i]

#    for i in range(len(A)):
#        if A[i] == 0:
#            totalPairs += prefixSum[-1] - prefixSum[i]

#    if totalPairs > 1000000000:
#        totalPairs = -1

#    return totalPairs
