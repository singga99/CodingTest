import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

a = set()
b = set()

for i in range(n):
    a.add(input().strip())

for i in range(m):
    b.add(input().strip())

result = sorted(a.intersection(b))

print(len(result))

for i in result:
    print(i)