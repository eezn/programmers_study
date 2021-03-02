def dfs(graph, vertex, visited):
    # 재귀적으로 처리하는 DFS
    visited[vertex] = 1
    print('{0} '.format(vertex))

    # 연결된 다른 노드 방문
    for n in graph[vertex]:
        if visited[n] == 0:
            dfs(graph, n, visited)


if __name__ == '__main__':
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    visited = [0] * 9

    dfs(graph, 1, visited)
