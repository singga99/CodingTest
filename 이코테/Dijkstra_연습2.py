# 개선된 코드
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한

n, m = map(int, input().strip().split())    # 노드 수, 간선 수
start = int(input().strip())    # 시작 노드 번호

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)    # 최단 거리 테이블

for i in range(m):
    a, b, c = map(int, input().strip().split()) # a -> b로 거리 c
    graph[a].append((b, c)) # 방향이 있어서 한 방향만 추가

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   # (거리, 노드)
    distance[start] = 0
    
    while q:
        dist, node = heapq.heappop(q)   # 거리와 노드 pop
        
        # 한 번 처리된 적 있는 노드면 무시
        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[1]  # 현재 노드의 거리 값
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance)