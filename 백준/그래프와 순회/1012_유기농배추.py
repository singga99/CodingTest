import sys
from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        a, b = q.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0 <= nx < m and 0 <= ny < n:
                if (field[nx][ny] == 1) and (visited[nx][ny] == False):
                    visited[nx][ny] = True
                    q.append((nx, ny))


input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    m, n, k = map(int, input().strip().split())  # 가로, 세로, 개수

    field = [[0] * n for _ in range(m)]
    for __ in range(k):
        x, y = map(int, input().strip().split())
        field[x][y] = 1

    visited = [[False] * n for _ in range(m)]

    result = 0
    for i in range(m):
        for j in range(n):
            if (field[i][j] == 1) and (visited[i][j] == False):
                bfs(i, j)
                result += 1

    print(result)