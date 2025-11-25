import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().strip().split())
start = int(input().strip())
INF = int(1e9)
distance = [INF] * (v+1)

# u -> v인 가중치 w
graph = [[] for _ in range(v+1)]
for i in range(e):
    u, v, w = map(int, input().strip().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        # 이미 한 번 처리된 노드는 넘어가기
        if distance[now] < dist:
            continue
        
        # 현재 노드와 연결된 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]  # 현재 노드의 거리 값 + 인접한 노드의 거리 값

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)