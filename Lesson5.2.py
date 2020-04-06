# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

String = 'CAGCCTA'
Array1 = [2, 5, 0, 4, 3]
Array2 = [4, 5, 6, 6, 4]

def solution(S, P, Q):
    # write your code in Python 3.6
    N = len(S)
    M = len(P)

    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    countSum = [{'A': 0, 'C': 0, 'G': 0, 'T': 0}]
    minImpact = []

    for i in range(N):
        counter[S[i]] += 1
        countSum.append(counter.copy())

    for j in range(M):
        start = P[j]
        end = Q[j] + 1

        if countSum[end]['A'] - countSum[start]['A'] > 0:
            minImpact.append(impact['A'])
        elif countSum[end]['C'] - countSum[start]['C'] > 0:
            minImpact.append(impact['C'])
        elif countSum[end]['G'] - countSum[start]['G'] > 0:
            minImpact.append(impact['G'])
        else:
            minImpact.append(impact['T'])

    return minImpact

print(solution(String, Array1, Array2))