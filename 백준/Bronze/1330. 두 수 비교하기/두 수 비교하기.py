import sys

def ginput():
    return sys.stdin.readline().rstrip()

a, b = map(int, ginput().split())

if a > b:
    print(">")
elif a == b:
    print("==")
else:
    print("<")