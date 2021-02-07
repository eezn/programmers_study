# brown, yellow = 10, 2 # return [4, 3]
# brown, yellow = 8, 1 # return [3, 3]
# brown, yellow = 24, 24 # return [8, 6]
brown, yellow = 2044, 20000
# brown, yellow = 12, 4

from math import sqrt


def is_prime(number):
    if number != 1:
        for f in range(2, number):
            if number % f == 0:
                return False
    else:
        return False
    return True


def solution(brown, yellow):
    factors = []
    root = int(sqrt(yellow))
    prime = is_prime(yellow)

    for i in range(yellow + 1, root, -1):
        for j in range(1, root + 1):
            if i * j == yellow:
                factors.append([i, j])

    if yellow == 1:
        return [3, 3]
    for a, b in factors:
        i = (a + b) * 2
        if prime and (yellow + 1) * 2 == i:
                return [a + 2, b + 2]
        elif i + 4 == brown:
                return [a + 2, b + 2]


if __name__ == "__main__":
    print(solution(brown, yellow))
