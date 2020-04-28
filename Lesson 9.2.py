array = [23171, 21011, 21123, 21366, 21013, 21367]

def solution(A):
    # write your code in Python 3.6
    maxProfit, lowDay = 0, 200000
    for i in A:
        lowDay = min(lowDay, i)
        maxProfit = max(maxProfit, i-lowDay)
    return maxProfit

print(solution(array))