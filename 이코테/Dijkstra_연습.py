# 간단한 코드 1
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한

n, m = map(int, input().strip().split())    # 노드 수, 간선 수
start = int(input().strip())    # 시작 노드 번호

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)   # 방문노드
distance = [INF] * (n+1)    # 최단 거리 테이블

for i in range(m):
    a, b, c = map(int, input().strip().split()) # a -> b로 거리 c
    graph[a].append((b, c)) # 방향이 있어서 한 방향만 추가

# 방문 X, 최단 거리의 짧은 노드 번호 반환
def small_node():
    index = 0
    min_v = INF
    for i in range(1, n+1):
        if (distance[i] < min_v) and (visited[i] == False):
            min_v = distance[i]
            index = i
    return index

# 다익스트라
def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    # 인접 노드의 거리 입력
    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작 노드 제외한 n-1개로 반복
    for i in range(n-1):
        now = small_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

print(distance)