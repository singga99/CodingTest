import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [sys.stdin.readline().strip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == '0':
                    visited[nx][ny] = True
                    queue.append((nx, ny))


# 0인 칸 and 방문 X -> BFS
result = 0
for i in range(n):
    for j in range(m):
        if (graph[i][j] == '0') and (visited[i][j] == False):
            bfs(i, j)
            result += 1


print(result)