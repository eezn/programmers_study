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
    if int(case_joined) == 0:
        return 0
    number_dictionary = dict()
    for value in numbers:
        split_value = list(str(value))
        print(split_value[0], value)
        number_category = split_value[0]
        if number_dictionary.get(number_category) is None:
            number_dictionary[number_category] = []
            number_dictionary[number_category].append(value)
        else:
            number_dictionary[number_category].append(value)
    # print(number_dictionary)

    ## 9 to 0 printer
    j = 9
    answer = []
    while j > 0:
        if number_dictionary.get(str(j)) is None:
            j -= 1
            continue
        number_values = number_dictionary.get(str(j))
        sorted_number_values = recurrence_reverse_sort(number_values)
        for value in sorted_number_values:
            answer.append(value)
        j -= 1

    answer = ''.join(map(str, answer))
    print(answer)


def recurrence_reverse_sort(numbers):
    # digit_colume = 10 ** current
    # print(digit_colume)
    sorted_numbers = []
    dynamic_length = len(numbers)

    sorted_numbers.append(numbers.pop())
    # print(digit_colume)

    print(numbers)

    return numbers


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
    numbers = [3, 30, 300, 94, 939, 9, 5, 0]
    # numbers = [0,0,0,0,0,0]
    print(solution_reverse_radix_sort(numbers))
