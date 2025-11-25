import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n+1)

cnt = 1
result = [0] * (n+1)
def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = True
    result[start] = cnt
    cnt += 1
    
    while q:
        v = q.popleft()
        graph[v].sort(reverse=True)

        for i in graph[v]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                result[i] = cnt
                cnt += 1

bfs(r)
print("\n".join(map(str, result[1:])))