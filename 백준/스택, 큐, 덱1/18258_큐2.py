import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
que = deque([])

for _ in range(n):
    s = input().strip().split()

    if len(s) == 2:
        a, b = s[0], int(s[1])
        que.append(b)

    else:
        s = s[0]
        if s == 'pop':
            if que:
                num = que.popleft()
                print(num)
            else:
                print(-1)
        
        elif s == 'size':
            print(len(que))
        
        elif s == 'empty':
            if que:
                print(0)
            else:
                print(1)

        elif s == 'front':
            if que:
                print(que[0])
            else:
                print(-1)
        
        elif s == 'back':
            if que:
                print(que[-1])
            else:
                print(-1)
