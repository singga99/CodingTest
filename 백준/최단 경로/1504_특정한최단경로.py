# 양방향
# 1. 임의로 주어진 두 정점 반드시 통과
# 2. 중복 통과 가능

import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().strip().split()) # a - b 연결(양방향), 거리 c
    graph[a].append((b, c)) # (노드, 거리)
    graph[b].append((a, c))

v1, v2 = map(int, input().strip().split())  # 반드시 거쳐야 하는 번호
start = 1
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))   # (거리, 노드)
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]  # 이전 거리 + 현재 노드의 거리 값
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # (거리, 노드)

    return distance

dist1, distv1, distv2 = 0, 0, 0

dist1 = dijkstra(start)
distv1 = dijkstra(v1)
distv2 = dijkstra(v2)

path1 = dist1[v1] + distv1[v2] + distv2[n]
path2 = dist1[v2] + distv2[v1] + distv1[n]

result = min(path1, path2)
print(result if result < INF else -1)