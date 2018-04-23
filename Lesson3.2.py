# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(X, Y, D):
    # write your code in Python 3.6
    Answer = math.ceil((Y-X) / D)
    return Answer

print(solution(10, 85, 30))