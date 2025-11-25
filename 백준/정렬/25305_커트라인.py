import sys

input = sys.stdin.readline

n, k = map(int, input().strip().split())
x = list(map(int, input().strip().split()))

x.sort(reverse=True)
print(x[k-1])