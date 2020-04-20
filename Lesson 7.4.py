array = [8, 8, 5, 7, 9, 8, 7, 4, 8]


def solution(H):
    count = 0
    stack = []

    for i in H:
        while len(stack) != 0 and stack[-1] > i:
            stack.pop()

        if len(stack) != 0 and stack[-1] == i:
            pass
        else:
            count += 1
            stack.append(i)

    return count


print(solution(array))