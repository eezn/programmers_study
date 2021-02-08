def soultion_001_tuple_sum(tuples):
    return tuples[0] + tuples[1]


def solution_001(jobs):
    # 첫번째 시도
    # 1. 대기시간과 작업시간의 합으로 가중치를 두고 정렬
    # 2. 이것을 수식으로 할것

    jobs = sorted(jobs, key=soultion_001_tuple_sum)
    # print(jobs)
    answer = 0
    previous_working_time = 0
    current_working_time = 0
    runtime_table = []
    for standby_time, working_time in jobs:
        current_working_time = working_time + previous_working_time
        # print(current_working_time)
        # print(current_working_time, standby_time, working_time)
        runtime = previous_working_time - standby_time + working_time
        # print(runtime)
        runtime_table.append(runtime)
        previous_working_time = current_working_time

    #     print("-----------------------")
    # print(runtime_table)
    avg_response_time = sum(runtime_table) // len(runtime_table)
    # for response_time in runtime_table:
    #     avg_response_time += response_time
    answer = avg_response_time
    return answer


if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]

    print(solution_001(jobs), 9)
    print(solution_001([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
    print(solution_001([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
    print(solution_001([[0, 3], [1, 9], [2, 6]]), 9)
    print(solution_001([[0, 1]]), 1)
    print(solution_001([[1000, 1000]]), 1000)
    print(solution_001([[0, 1], [0, 1], [0, 1]]), 2)
    print(solution_001([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
    print(solution_001([[0, 1], [1000, 1000]]), 500)
    print(solution_001([[100, 100], [1000, 1000]]), 500)
    print(solution_001([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
    print(solution_001([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)
