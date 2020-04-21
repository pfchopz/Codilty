array = [3, 4, 3, 2, 3, -1, 3, 3]

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    size = 0
    for i in range(n):
            if size == 0:
                size += 1
                value = A[i]
            else:
                if value != A[i]:
                    size -= 1
                else:
                    size += 1
    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if A[k] == candidate:
            count += 1
            leaderPosition = k
    if count > n // 2:
        leader = candidate
        return leaderPosition
    return -1

print(solution(array))