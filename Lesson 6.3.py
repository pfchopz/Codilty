TestArray = [1, 5, 2, 1, 4, 0]

def solution(A):
    # write your code in Python 3.6
    # declare variables
    length = len(A)
    intersect_count = 0
    right_intersect = [0] * length
    right_intersect_prefixsums = [0] * length


# populate right_intersect with right intersection counts
    for idx, value in enumerate(A):
        if (idx + value) >= length:
            right_intersect[-1] += 1
        else:
            right_intersect[idx + value] += 1

# calculate prefix sums for intersections
    for i in range(1, length):
        if i == 1:
            right_intersect_prefixsums[i] += (right_intersect[i - 1] + right_intersect[i])
        else:
            right_intersect_prefixsums[i] += (right_intersect_prefixsums[i - 1] + right_intersect[i])


    print(right_intersect)
    print(right_intersect_prefixsums)





print(solution(TestArray))