def solution(n, edge):
    # n개의 2차원 배열 만들어서 vertex의 인접 매트릭스 생성
    vertex_matrix = [[0 for col in range(n)] for row in range(n)]
    print('인접 매트릭스 생성 : {0}'.format(vertex_matrix))

    # 받은 vertex 그래프 밀어넣기
    for node in edge:
        vertex_matrix[node[0] - 1][node[1] - 1] = 1  # -1 하는 이유는 배열은 0부터 시작하고 입력 vertex value는 1부터 시작하기 때문
        vertex_matrix[node[1] - 1][node[0] - 1] = 1  # undirected graph라서 뒤집어서도 넣어야 연결이 성립됨.
    print('인접 매트릭스 완성 : {0}'.format(vertex_matrix))
    for vertex in vertex_matrix:
        print(vertex)

    print('------------------------')
    # 매트릭스 순회하기.

    ## 뭔가 재귀처리를 해야할거같은데 DFSBFS 찾다가 포기한 코드.........

    far_count = 0
    visited_vertex = [0 for elem in range(n)]
    visited_vertex[0] = 1  # 자기 자신은 방문한 상태기 때문.

    for n in range(len(vertex_matrix[0])):
        if n != 0:
            if vertex_matrix[0][n] == 1:
                far_count += 1
                visited_vertex[n] = 1
    print('방문한 vertex : {0}'.format(visited_vertex))
    answer = 0
    return answer


def visit_vertex(vertex_matrix, visiting, visited_vertex):
    for n in range(len(visited_vertex)):
        if visited_vertex[n] == 0:
            vertex_matrix[visiting]
            pass
    return 1
    return 0
