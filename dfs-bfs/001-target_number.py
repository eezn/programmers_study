numbers_01 = [1, 1, 1, 1, 1]
target_01 = 3

numbers_02 = [4, 3, 3, 1, 2]
target_02 = 5

# 모든 숫자를 다 사용해야 함
# 문자열로 만들어진 수식 계산 -> eval(string)


# 1. +, - 로 분기되는 재귀함수(X)
def rec_001(numbers, target, idx):
    if idx < len(numbers):
        return "+" + str(numbers[idx]) + rec_001(numbers, target, idx+1)
    else:
        return ""


def solution_001(numbers, target):
    answer = 0
    numbers.sort()
    print(rec_001(numbers, target, 0))
    print(eval(rec_001(numbers, target, 0)))
    return answer


# 2. 재귀함수2(O)
def solution_002(numbers, target):
    if not numbers:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution_002(numbers[1:], target + numbers[0]) + solution_002(numbers[1:], target - numbers[0])


# Brute Force(O)
def solution_003(numbers, target):
    answer = 0
    current_list = [numbers[0], -numbers[0]]

    for i in range(1, len(numbers)):
        next_number = numbers[i]
        next_list = []
        for num in current_list:
            next_list.append(num + next_number)
            next_list.append(num - next_number)

        current_list = next_list

    for num in current_list:
        if num == target:
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution_002(numbers_01, target_01))
    print(solution_002(numbers_02, target_02))

    print(solution_003(numbers_01, target_01))
    print(solution_003(numbers_02, target_02))
