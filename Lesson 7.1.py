String = '{{{{'

def solution(S):
    # write your code in Python 3.6
    dict = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for i in S:
        if i in dict:
            stack.append(dict[i])
        elif not stack:
            return 0
        else:
            if stack.pop() != i:
                return 0

    if not stack:
        return 1
    else:
        return 0

print(solution(String))