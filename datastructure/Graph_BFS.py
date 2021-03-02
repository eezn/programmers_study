from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        visit = queue.popleft()
        print('{0} '.format(visit))
        for n in graph[visit]:
            if visited[n] == 0:
                queue.append(n)
                visited[n] = 1


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

    bfs(graph, 1, visited)
