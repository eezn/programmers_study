numbers1 = "17"
numbers2 = "011"

from math import sqrt
from itertools import permutations


def is_prime(number):
    if number < 2:
        return 0
    elif number == 2 or number == 3:
        return 1
    else:
        i = 2
        root = sqrt(number)
        while i <= root:
            if number % i == 0:
                return 0
            i += 1
        return 1


def solution(numbers):
    answer = 0
    lst = []
    for i in range(1, len(numbers) + 1):
        for item in permutations(numbers, i):
            lst.append(int("".join(item)))

    for item in set(lst):
        if is_prime(item):
            answer += 1
    return answer


if __name__ == "__main__":
    print(solution(numbers1))