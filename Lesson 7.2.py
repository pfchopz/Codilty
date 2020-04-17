arrayA = [4, 3, 2, 1, 5]
arrayB = [0, 1, 0, 0, 0]

def solution(A, B):
    # write your code in Python 3.6
    upstreamStack = []
    totalFish = 0

    for i in range(len(A)):
        if B[i] == 0:
            if not upstreamStack:
                totalFish += 1
            else:
                while upstreamStack:
                    upstreamFish = upstreamStack.pop()
                    if A[i] > upstreamFish:
                        pass
                    else:
                        upstreamStack.append(upstreamFish)
                        break
                if not upstreamStack: totalFish += 1
        else:
            upstreamStack.append(A[i])

    return totalFish + len(upstreamStack)

print(solution(arrayA, arrayB))