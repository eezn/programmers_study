# brown, yellow = 10, 2 # return [4, 3]
# brown, yellow = 8, 1 # return [3, 3]
brown, yellow = 24, 24 # return [8, 6]
# brown, yellow = 2044, 20000
# brown, yellow = 12, 4


from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    elif number == 2 or number == 3:
        return True
    else:
        i = 2
        root = sqrt(number)
        while i <= root:
            if number % i == 0:
                return False
            i += 1
        return True


def solution(brown, yellow):
    factorizations = dict()
    root = int(sqrt(yellow))
    prime = is_prime(yellow)

    if yellow == 1:
        return [3, 3]

    for f in range(2, root + 1):
        count = 0
        if is_prime(f):
            while (yellow % f) == 0:
                count += 1
                yellow /= f
            if count:
                factorizations.setdefault(f, count)
    print(factorizations)


if __name__ == "__main__":
    print(solution(brown, yellow))