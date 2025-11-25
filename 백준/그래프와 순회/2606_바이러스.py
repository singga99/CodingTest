import sys
from collections import deque

computer = int(sys.stdin.readline().strip())
connect_com = int(sys.stdin.readline().strip())

network = [[] for _ in range(computer + 1)]
for _ in range(connect_com):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    network[v1].append(v2)
    network[v2].append(v1)

visited = [False] * (computer+1)

def bfs(start):
    cnt = 0
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        v = q.popleft()
    
        for i in network[v]:
            if visited[i] == False:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt

print(bfs(1))