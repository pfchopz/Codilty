# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

TestArray = [9, 3, 9, 3, 9, 7, 9, 7, 7, 7]

def solution(A):
    # write your code in Python 3.6
    c = Counter(A)
    for i in c:
        if c[i] % 2 != 0:
            return i

print(solution(TestArray))