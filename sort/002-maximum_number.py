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
    case_joined = ''.join(map(str, numbers))
    if int(case_joined) == 0 :
        return 0
    pointer_list = []
    for value in numbers:
        split_value = list(str(value))
        print(split_value[0])


def solution_use_permutations(numbers):
    # case_joined = ''.join(map(str, numbers))
    # if int(case_joined) == 0 :
    #     return 0
    permuted_list = list(permutations(numbers, len(numbers)))
    joined_list = []
    # print(permuted_list)
    for value in permuted_list:
        string = ''.join(map(str, value))
        # print(string)
        if int(string) == 0:
            joined_list.append(0)
            break
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
    numbers = [3, 30, 34, 5, 9, 0]
    # numbers = [0,0,0,0,0,0]
    print(solution_reverse_radix_sort(numbers))
