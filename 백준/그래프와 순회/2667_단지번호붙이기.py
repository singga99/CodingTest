import sys
from collections import deque

n = int(sys.stdin.readline().strip())
house_map = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip()))
    house_map.append(row)


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        a, b = q.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if (0 <= nx < n) and (0 <= ny < n):
                if (house_map[nx][ny] == 1) and (visited[nx][ny] == False):
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return cnt

visited = [[False] * n for _ in range(n)]

house = 0   # 단지 개수
house_cnt = [] # 단지 내 집의 수
for i in range(n):
    for j in range(n):
        if (house_map[i][j] == 1) and (visited[i][j] == False):
            house_cnt.append(bfs(i, j))
            house += 1

print(house)
house_cnt.sort()
for f in house_cnt:
    print(f)