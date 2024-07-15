import sys

def ginput():
    return sys.stdin.readline().rstrip()

a, b = map(int, ginput().split())
print(a / b)