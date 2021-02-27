# 정답코드


def solution(n, edge):
    import collections
    answer = [1] + [0] * (n - 1)
    vec = [[] for i in range(n)]
    que = collections.deque([1])
    for i in edge:
        vec[i[0] - 1].append(i[1])
        vec[i[1] - 1].append(i[0])
    while que:
        l = len(que)
        for i in range(l):
            q = que.popleft()
            for e in vec[q - 1]:
                if answer[e - 1] == 0:
                    answer[e - 1] = 1
                    que.append(e)
    return l


if __name__ == '__main__':
    n = 6
    vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print('{0}'.format(solution(n, vertex)))
