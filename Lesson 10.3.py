def solution(N):
    # write your code in Python 3.6
    i = 1
    d1 = 0
    while i * i < N:
        if (N % i == 0):
            d1 = i
        i += 1
    if (i * i == N):
        return int(2 * (i + i))
    d2 = N / d1
    return int(2 * (d1 + d2))

print(solution(36))