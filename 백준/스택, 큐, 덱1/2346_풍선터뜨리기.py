import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
balloon = deque(range(1, n+1))
que = deque(map(int, input().strip().split()))


# 처음 1번 풍선
x = balloon.popleft()
print(x)
