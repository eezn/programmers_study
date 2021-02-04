p1 = [1, 2, 3, 2, 3]
# return = [4, 3, 1, 1, 0]
p2 = [2, 4, 5, 6, 1, 2, 2, 3, 3]
p3 = [1, 1, 1, 1, 1, 2, 3, 2]


def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        count = 0
        j = i + 1
        while j < len(prices):
            count += 1
            if prices[i] > prices[j]:
                break
            j += 1
        answer.append(count)
    answer.append(0)
    return answer


if __name__ == "__main__":
    print(solution(p1))
    print(solution(p2))
    print(solution(p3))
