import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())
que = deque(range(1, n+1))
result = []

check = 1
while que:
    x = que.popleft()

    if check != k:
        que.append(x)
        check += 1
    else:
        result.append(str(x))
        check = 1

print(f"<{', '.join(result)}>")