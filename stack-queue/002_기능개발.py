p1 = [93, 30, 55]
s1 = [1, 30, 5]
# return = [2, 1]

p2 = [95, 90, 99, 99, 80, 99]
s2 = [1, 1, 1, 1, 1, 1, 1]
# return = [1, 3, 2]


def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    for i in range(length):
        progresses[i] = 100 - progresses[i]
        days = 1
        while progresses[i] > speeds[i] * days:
            days += 1
        progresses[i] = days
    print(progresses)

    start = 0
    while start < length:
        end = start + 1
        while end < length:
            if progresses[start] >= progresses[end]:
                end += 1
            else:
                break
        answer.append(end - start)
        start = end
    return answer


if __name__ == "__main__":
    print(solution(p1, s1))
    print(solution(p2, s2))
