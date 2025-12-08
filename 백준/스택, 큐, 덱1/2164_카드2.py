import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
que = deque([i for i in range(1, n+1)])

while len(que) > 1:
    que.popleft()
    x = que.popleft()
    que.append(x)

print(que[0])

# while len(que) > 1:
#     for i in range(2):
#         if i == 0:
#             que.popleft()
        
#         else:
#             x = que.popleft()
#             que.append(x)
        

# print(que[0])