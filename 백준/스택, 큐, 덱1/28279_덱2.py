import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
que = deque()

for _ in range(n):
    s = input().strip().split()

    if len(s) == 2:
        a, b = int(s[0]), int(s[1])
        if a == 1:
            que.appendleft(b)
        else:
            que.append(b)

    else:
        s = int(s[0])
        if s == 3:
            if que:
                x = que.popleft()
                print(x)
            else:
                print(-1)
        
        elif s == 4:
            if que:
                x = que.pop()
                print(x)
            else:
                print(-1)
        
        elif s == 5:
            print(len(que))
        
        elif s == 6:
            print(0 if que else 1)
        
        elif s == 7:
            print(que[0] if que else -1)
        
        elif s == 8:
            print(que[-1] if que else -1)