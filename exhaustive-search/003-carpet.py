# brown, yellow = 10, 2 # return [4, 3]
# brown, yellow = 8, 1 # return [3, 3]
brown, yellow = 24, 24 # return [8, 6]


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
    isprime = is_prime(yellow)
    for i in range(yellow + 1, 1, -1):
        for j in range(1, root + 1):
            if i * j == yellow:
                factorizations.append([i, j])
    # print(factorizations)

    if yellow == 1:
        return [3, 3]
    for a, b in factorizations:
        print(a, b)
        if isprime:
            if (yellow + 1) * 2 == 2 * (a + b):
                return [a + 2, b + 2]
        else:
            if yellow - 4 == 2 * (a + b):
                return [a + 2, b + 2]


if __name__ == "__main__":
    print(solution(brown, yellow))
