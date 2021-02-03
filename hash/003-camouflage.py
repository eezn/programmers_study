##
#
from itertools import combinations

c1_t = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

c1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
c2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

###

t1 = [
    ["a", "1"],
    ["b", "1"],
    # ["c", "1"],
    ["A", "2"],
    ["B", "2"],
    # ["C", "2"],
    ["!", "3"],
    ["@", "3"],
    # ["#", "3"]
]  ## 6 + 12 + 8 = 26개

t2 = [
    ["a", "1"],
    ["b", "1"],
    ["c", "1"],
    ["A", "2"],
    # ["B", "2"],
    # ["C", "2"],
    ["!", "3"],
    ["@", "3"],
    # ["#", "3"]
]  ## 6 + 11 + 6 = 23개

t3 = [
    ["a", "가"],
    ["b", "가"],
    ["c", "가"],
    ["A", "나"],
    ["B", "나"],
    ["C", "나"],
    ["!", "다"],
    ["@", "다"],
    ["#", "다"]
]  ## 63개

t4 = [
    ["a", "가"],
    ["A", "나"],
    ["#", "다"],
    ["X", "라"],
    ["S", "마"],
    ["R", "바"],
]  ## 63


###
def solution(clothes):
    a = 0
    set_data = set()
    for i in clothes:
        # print(i[0])
        set_data.add(i[0])
        a += 1
        for j in clothes:
            t1 = i[0] + "+" + j[0]
            t2 = j[0] + "+" + i[0]
            # print(t1, t2)
            if i[1] == j[1]:
                continue
            if t1 == t2:
                continue
            if t1 not in set_data and t2 not in set_data:
                set_data.add(t1)
                # print(t1)
                a += 1
    # print(set_data)
    # print(a)
    return a


def solution_use_dict(clothes):
    attribute = dict()
    for v in clothes:
        v
    for value, key in clothes:
        if attribute.get(key) is None:
            attribute[key] = []
            attribute[key].append(value)
        else:
            attribute[key].append(value)
    # print(attribute)
    count = 0

    set_attribute = set()
    keys = list(attribute.keys())

    keys = iter(list(attribute.keys()))
    # print(keys)
    #
    while True:
        try:
            current_pointer = next(keys)
            print(current_pointer)
            next_pointer = next(keys)
            print(next_pointer)

        except StopIteration:
            break

    print(count)
    answer = 0
    return answer


def solution_use_dict2(clothes):
    attribute = dict()
    entity = dict()
    for value, key in clothes:
        if attribute.get(key) is None:
            attribute[key] = []
            attribute[key].append(value)
        else:
            attribute[key].append(value)
    print(attribute)
    keys_list = list(attribute.keys())
    keys_len = len(keys_list)
    print("keys_len : " + str(keys_len))

    value_list = []
    for key in keys_list:
        entity[key] = len(attribute.get(key))
        # count += len(attribute.get(key))
        for value in attribute.get(key):
            value_list.append(value)
    print("entity_list : " + str(entity))


def solution_use_combinations(clothes):
    attribute = dict()
    entity = dict()
    for value, key in clothes:
        if attribute.get(key) is None:
            attribute[key] = []
            attribute[key].append(value)
            entity[key] = len(attribute[key])
        else:
            attribute[key].append(value)
            entity[key] = len(attribute[key])
    print(attribute)
    keys_list = list(attribute.keys())
    keys_len = len(keys_list)
    print("keys_len : " + str(keys_len))
    print("entity : " + str(entity))

    solo_num = sum(entity.values())
    print("1개를 고를 때 :" + str(solo_num))

    sum_num = 0
    for i in range(2, keys_len + 1):
        key_list_combinations = list(combinations(entity, i))
        print(str(i) + "개를 고를 때 :" + str(key_list_combinations))
        for j in range(len(key_list_combinations)):
            print(key_list_combinations[j])
            multiply_num = 0
            for k in range(len(key_list_combinations[j])):
                if multiply_num == 0:
                    multiply_num = len(attribute.get(key_list_combinations[j][k]))
                else:
                    multiply_num *= len(attribute.get(key_list_combinations[j][k]))
            sum_num += multiply_num
            print(str(multiply_num) + "가지 경우의 수")
        print("를 더해서 " + str(sum_num))

    print(str(solo_num) + " + " + str(sum_num))
    return solo_num + sum_num


def solution_use_combinations1(clothes):
    attribute = dict()
    entity = dict()
    for value, key in clothes:
        if attribute.get(key) is None:
            attribute[key] = []
            attribute[key].append(value)
            entity[key] = len(attribute[key])
        else:
            attribute[key].append(value)
            entity[key] = len(attribute[key])
    keys_list = list(attribute.keys())
    keys_len = len(keys_list)

    solo_num = sum(entity.values())

    sum_num = 0
    for i in range(2, keys_len + 1):
        key_list_combinations = list(combinations(entity, i))
        for j in range(len(key_list_combinations)):
            multiply_num = 0
            for k in range(len(key_list_combinations[j])):
                if multiply_num == 0:
                    multiply_num = len(attribute.get(key_list_combinations[j][k]))
                else:
                    multiply_num *= len(attribute.get(key_list_combinations[j][k]))
            sum_num += multiply_num

    return solo_num + sum_num


def factorial(n):
    i = n
    answer = 0
    while True:
        if n == 1:  # 1! = 1
            return 1
        elif answer == 0:  # 초기값 계산
            answer = i * (i - 1)
        else:  # 그 뒤로 반복
            answer = answer * (i - 1)
        i -= 1
        if i <= 1:
            break
    return answer


def recurrence_factorial(n):
    answer = n
    if n > 1:
        answer = n * recurrence_factorial(n - 1)
    return answer


if __name__ == '__main__':
    # solution(c1_t)
    n = 9
    # print(factorial(n))
    # print(recurrence_factorial(n))
    print(solution_use_combinations(t2))
