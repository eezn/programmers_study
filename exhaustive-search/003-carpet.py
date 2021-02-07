# brown, yellow = 10, 2 # return [4, 3]
# brown, yellow = 8, 1 # return [3, 3]
# brown, yellow = 24, 24 # return [8, 6]
brown, yellow = 2044, 20000
# brown, yellow = 12, 4

from math import sqrt


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


def solution(brown, yellow):
    factorizations = []
    root = int(sqrt(yellow))
    prime = is_prime(yellow)

    for i in range(yellow + 1, root - 1, -1):
        for j in range(1, root + 1):
            if i * j == yellow:
                factorizations.append([i, j])

    if yellow == 1:
        return [3, 3]
    for a, b in factorizations:
        print(a, b)
        if prime and (yellow + 1) * 2 == (a + b) * 2:
                return [a + 2, b + 2]
        elif (a + b) * 2 + 4 == brown:
                return [a + 2, b + 2]


if __name__ == "__main__":
    print(solution(brown, yellow))
