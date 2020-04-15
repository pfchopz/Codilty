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
        radius_coverage = idx + value
        if radius_coverage >= length:
            for i in range(idx, length):
                right_intersect[i] += 1
        else:
            for i in range(idx, radius_coverage + 1):
                right_intersect[i] += 1

# calculate prefix sums for intersections
#    for i in range(1, length):
#        if i == 1:
#            right_intersect_prefixsums[i] += (right_intersect[i - 1] + right_intersect[i])
#        else:
#            right_intersect_prefixsums[i] += (right_intersect_prefixsums[i - 1] + right_intersect[i])


#    print(right_intersect)
#    print(right_intersect_prefixsums)


# count intersections
    for j in range(1, length):
        left_intersect = j - A[j]

        if A[j] == 0:
            intersect_count += right_intersect[j]
        elif left_intersect > 0:
            temp = right_intersect[left_intersect : j]
            intersect_count += sum(temp) // max(temp)
        else:
            temp = right_intersect[0 : j]
            intersect_count += sum(temp) // max(temp)

    return intersect_count

print(solution(TestArray))