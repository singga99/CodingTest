def dfs(graph, start, visited):
    visited[start] = True
    stack = [start]
    print(start)

    for i in graph[start]:
        if visited[i] == False:
            stack.append(i)
            visited[i] = True
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)