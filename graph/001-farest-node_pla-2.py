# 정답코드

# n : 노드의 개수, edge : 노드간 간선 관계
def solution(n, edge):
    import collections
    visited = [1] + [0] * (n - 1)
    adj_list = [[] for i in range(n)]
    queue = collections.deque([1])
    for elem in edge:
        adj_list[elem[0] - 1].append(elem[1])
        adj_list[elem[1] - 1].append(elem[0])
    while queue:
        length = len(queue)
        for i in range(length):
            q = queue.popleft()
            for e in adj_list[q - 1]:
                if visited[e - 1] == 0:
                    visited[e - 1] = 1
                    queue.append(e)
    return length


if __name__ == '__main__':
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print('{0}'.format(solution(n, edge)))
