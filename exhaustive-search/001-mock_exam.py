answers = [1, 2, 3, 4, 5]


def solution(answers):
    answer = []
    scores = [0, 0, 0]
    patterns = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for idx, elem in enumerate(answers):
        if elem == patterns[0][idx % 5]:
            scores[0] += 1
        if elem == patterns[1][idx % 8]:
            scores[1] += 1
        if elem == patterns[2][idx % 10]:
            scores[2] += 1
    print(scores)

    for idx in range(len(scores)):
        if scores[idx] == max(scores):
            answer.append(idx + 1)
    return answer


if __name__ == "__main__":
    solution(answers)
