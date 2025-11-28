import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

s = set()
for i in range(n):
    s.add(input().strip())

test = []
for j in range(m):
    test.append(input().strip())

cnt = 0
for t in test:
    if t in s:
        cnt += 1

print(cnt)