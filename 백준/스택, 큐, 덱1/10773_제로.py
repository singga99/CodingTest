import sys

input = sys.stdin.readline

k = int(input().strip())
stack = []

for _ in range(k):
    n = int(input().strip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))