# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

Test = 561892

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    a = 0
    b = 0

    for i in binary:
        if i == '0':
            a += 1
        else:
            if b < a:
                b = a
                a = 0
            else:
                a = 0

    return b

print(solution(Test))