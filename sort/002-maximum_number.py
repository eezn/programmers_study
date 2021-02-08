#
#
import functools
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


###

def solution_reverse_radix_sort(numbers):
    case_joined = ''.join(map(str, numbers))
    if int(case_joined) == 0:
        return 0
    number_dictionary = dict()
    for value in numbers:
        split_value = list(str(value))
        # print(split_value[0], value)
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
    while j >= 0:
        if number_dictionary.get(str(j)) is None:
            j -= 1
            continue
        number_values = number_dictionary.get(str(j))
        # print(number_values)
        sorted_number_values = sort_by_order(number_values)
        for value in sorted_number_values:
            answer.append(value)
        j -= 1

    answer = ''.join(map(str, answer))
    # print(answer)
    return answer


def sort_by_order(numbers):
    # digit_colume = 10 ** current
    # print(digit_colume)

    temp_numbers = []
    # print(numbers)
    for number in numbers:
        temp_numbers.append(''.join(reversed(str(number))))
    # temp_numbers.sort()
    print(temp_numbers)

    one_numbers = []
    ten_numbers = []
    hundred_numbers = []

    for number in temp_numbers:
        # print(number[-1])
        if len(number) == 1:
            one_numbers.append(str(number))
            # print("one : "+str(one_numbers))
        elif len(number) == 2:
            ten_numbers.append(''.join(reversed(str(number))))
            ten_numbers.sort(reverse=True)
            # print("ten : "+str(ten_numbers))
        elif len(number) == 3:
            hundred_numbers.append(''.join(reversed(str(number))))
            hundred_numbers.sort(reverse=True)
            # print("hundred : "+str(hundred_numbers))
    print("one : " + str(one_numbers))
    print("ten : " + str(ten_numbers))
    print("hundred : " + str(hundred_numbers))
    # print(one_numbers, ten_numbers, hundred_numbers)
    sorted_numbers = one_numbers + ten_numbers + hundred_numbers
    print(sorted_numbers)
    # sorted_numbers.append(numbers.pop())
    # print(digit_colume)

    # print(sorted_numbers)

    return sorted_numbers


def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return int(t1) - int(t2)


def solution_pass(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    return str(int(''.join(n)))


if __name__ == '__main__':
    # numbers = [6, 10, 2]
    # numbers = [3, 30, 34, 5, 9, 0]
    numbers = [3, 30, 300, 94, 939, 9, 5, 0]
    numbers = [3, 30, 34, 5, 9]
    # numbers = [0,0,0,0,0,0]
    print(numbers)
    print(solution_pass(numbers))
