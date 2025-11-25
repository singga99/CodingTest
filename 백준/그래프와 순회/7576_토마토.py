import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())

farm = [[] for _ in range(m)]
for i in range(m):
    farm[i] = list(map(int, input().strip().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()

for i in range(m):
    for j in range(n):
        if farm[i][j] == 1:
            q.append((i, j))


def bfs():
    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < m) and (0 <= ny < n):
                if (farm[nx][ny] == 0):
                    q.append((nx, ny))
                    farm[nx][ny] = farm[a][b] + 1

bfs()

answer = 0
for i in range(m):
    for j in range(n):
        if farm[i][j] == 0:
            print(-1)
            sys.exit()
        answer = max(answer, farm[i][j])

print(answer-1)