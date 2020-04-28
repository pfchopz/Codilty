array = [3, 2, 6, -1, 4, 5, -1, 2]

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    starts, ends = [0] * N, [0] * N
    for i in range(1,N-1):
        left, right = i, N-i-1
        starts[left] = max(starts[left - 1] + A[left], 0)
        ends[right] = max(ends[right + 1] + A[right], 0)
    return max((starts[i-1] + ends[i+1] for i in range(1, N-1)))

print(solution(array))




#def solution(A):
    # write your code in Python 3.6
#    N = len(A)
#    max_ending = max_slice = 0
#    low_candidate = low_leader = 0
#    for i in range(1, N - 2):
#        max_ending = max(0, max_ending + A[i])
#        max_slice = max(max_slice, max_ending)

#        if max_ending == 0:

#        if max_ending > 0  and low_candidate > A[i]:
#            low_candidate = A[i]

