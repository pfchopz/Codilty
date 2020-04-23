array = [4, 3, 4, 4, 4, 2]

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
    if count > n // 2:
        leader = candidate
    countRight = count
    countLeft = 0
    equiCount = 0
    for j in range(n):
        if A[j] == leader:
            countLeft += 1
            countRight -= 1
        if countLeft > (j + 1) // 2 and countRight > (n - j - 1) // 2:
            equiCount += 1
    return equiCount

print(solution(array))