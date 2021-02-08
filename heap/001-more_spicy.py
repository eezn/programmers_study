import heapq
from collections import deque


def solution_001(scoville, K):
    # 첫번째 시도
    # 1. scoville 정렬 -> 데크 밀어넣기
    # 2. K 이상이 될 때 까지 while
    # -> 테스트 통과하지만 채점 불가능.
    scoville_deque = deque(scoville)
    # scoville_deque.sort()
    temp_K = 0
    count = 0
    while temp_K < K:
        try:
            temp_K = scoville_deque.popleft() + (scoville_deque.popleft() * 2)
            count += 1
        except:
            return -1
        finally:
            if temp_K < K:
                scoville_deque.appendleft(temp_K)

    # print(scoville_deque)
    return count


def solution_003(scoville, K):
    # 세번째 시도
    # 힌트를 얻은 heapq 시도
    # -> 테스트 통과하지만 채점 불가
    heapq.heapify(scoville)
    temp_K = 0
    count = 0
    while temp_K < K:
        try:
            temp_K = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            count += 1
        except:
            return -1
        finally:
            if temp_K < K:
                heapq.heappush(scoville, temp_K)

    # print(scoville)
    return count


def solution_004(scoville, K):
    # 네번째 (정답코드)
    # 첫번째 원소에서 가장 큰 스코빌 지수에 대한 예외처리
    # 이런건 상상도 못한 정체 ㄴㅇㄱ
    heapq.heapify(scoville)
    answer = 0
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1

    return answer


if __name__ == '__main__':
    scoville1 = [1, 2, 3, 9, 10, 12]
    K1 = 7
    print(solution_003(scoville1, K1))

    ## 이하 테스트 케이스 공유
    print(solution_003([1, 1, 1], 4), 2)
    print(solution_003([10, 10, 10, 10, 10], 100), 4)
    print(solution_003([1, 2, 3, 9, 10, 12], 7), 2)
    print(solution_003([0, 2, 3, 9, 10, 12], 7), 2)
    print(solution_003([0, 0, 3, 9, 10, 12], 7), 3)
    print(solution_003([0, 0, 0, 0], 7), -1)
    print(solution_003([0, 0, 3, 9, 10, 12], 7000), -1)
    print(solution_003([0, 0, 3, 9, 10, 12], 0), 0)
    print(solution_003([0, 0, 3, 9, 10, 12], 1), 2)
    print(solution_003([0, 0], 0), 0)
    print(solution_003([0, 0], 1), -1)
    print(solution_003([1, 0], 1), 1)
