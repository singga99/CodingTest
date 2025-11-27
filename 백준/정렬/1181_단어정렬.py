import sys

input = sys.stdin.readline

n = int(input().strip())

arr = []
for i in range(n):
    s = input().strip()
    if s not in arr:
        arr.append(s)

arr.sort(key=lambda x:(len(x), x))
for i in arr:
    print(i)