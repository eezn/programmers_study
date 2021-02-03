#
#
from itertools import permutations


def solution_insert_sort(numbers):
    i = 1
    while i < len(numbers):
        j = i
        # print(numbers[i - 1], numbers[i])
        while j > 0 and (str(numbers[j - 1]) + str(numbers[j])) < (str(numbers[j]) + str(numbers[j - 1])):
            # print((str(numbers[j - 1]) + str(numbers[j])) < (str(numbers[j]) + str(numbers[j - 1])))
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
            print(numbers)
            j -= 1
        i += 1
    answer = str(''.join(map(str, numbers)))
    return answer


def solution_reverse_radix_sort(numbers):
    pass


def solution_use_permutations(numbers):
    permuted_list = list(permutations(numbers, len(numbers)))
    joined_list = []
    for value in permuted_list:
        string = ''.join(map(str, value))
        joined_list.append(string)
    joined_list.sort(reverse=True)
    return str(joined_list[0])


def solution_test(numbers):
    i = 1
    while i < len(numbers):
        print(list(str(numbers[i - 1]))[0], list(str(numbers[i]))[0])
        if list(str(numbers[i - 1]))[0] < list(str(numbers[i]))[0]:
            print("wow?")
        i += 1


if __name__ == '__main__':
    # numbers = [6, 10, 2]
    numbers = [3, 30, 34, 5, 9]
    print(solution_insert_sort(numbers))
