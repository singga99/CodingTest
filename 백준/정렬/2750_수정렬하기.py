import sys

input = sys.stdin.readline

n = int(input().strip())
arr = []
for _ in range(n):
    num = int(input().strip())
    arr.append(num)

arr.sort()
for i in arr:
    print(i)