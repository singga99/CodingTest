import sys

input = sys.stdin.readline

a, b = map(int, input().strip().split())

a_s = set(map(int, input().strip().split()))
b_s = set(map(int, input().strip().split()))

result = a_s.difference(b_s)
result2 = b_s.difference(a_s)

print(len(result) + len(result2))