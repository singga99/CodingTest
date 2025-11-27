import sys

input = sys.stdin.readline

n = int(input().strip())
arr = []

for i in range(n):
    x, y = map(int, input().strip().split())
    arr.append([y, x])

arr.sort()
for i in arr:
    print(*i[::-1])