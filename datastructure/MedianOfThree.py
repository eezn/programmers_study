import copy


def find_pivot(array):
    print("---배열의 처음, 중간, 마지막 인덱스 구하기---")
    data_array = array
    median_index = (len(data_array) // 2)
    print(0, median_index, len(data_array))

    print("---인덱스에 따른 배열의 값 깊은복사 (기존 데이터 변화없음)---")
    first_value = copy.deepcopy(data_array[0])
    median_value = copy.deepcopy(data_array[median_index])
    last_value = copy.deepcopy(data_array[-1])
    print(first_value, median_value, last_value)
    print(data_array)

    print("---3개의 값을 정렬---")
    arrange_three_value = [first_value, median_value, last_value]
    arrange_three_value.sort()
    print(arrange_three_value)

    print("---정렬된 값을 다시 밀어넣고 중간값은 따로 빼기---")
    # array.insert(0, copy.deepcopy(arrange_three_value[0]))
    # array.insert(median_index, copy.deepcopy(arrange_three_value[2]))
    data_array[0] = copy.deepcopy(arrange_three_value[0])
    return_median_value = copy.deepcopy(arrange_three_value[1])
    data_array[median_index] = copy.deepcopy(arrange_three_value[2])
    data_array[-1] = 0
    print(return_median_value, data_array)

    r = (return_median_value, data_array)
    return r


def find_pivot_value(array):
    r = find_pivot(array)
    return r[0]


def find_pivot_index(array, first_index, median_index, last_index):
    if array[median_index] < array[first_index]:
        array[median_index], array[first_index] = array[first_index], array[median_index]

    if array[last_index] < array[median_index]:
        array[last_index], array[median_index] = array[median_index], array[last_index]

    if array[median_index] < array[first_index]:
        array[median_index], array[first_index] = array[first_index], array[median_index]
    return copy.deepcopy(array[median_index])


if __name__ == '__main__':
    data = [4, 2, 5, 7, 9, 10, 1, 3, 8, 6, 11]
    # data = [32, 77, 49, 35, 61, 48, 73, 23, 95, 3, 89, 37, 23, 99, 17, 32, 94, 28, 15, 55, 7, 51, 88, 97, 57]

    print("---피벗을 찾고자 하는 데이터---")
    print(data)
    refine_data = find_pivot(data)

    print("---정렬 완료 후---")
    print(refine_data)

    print("---출력된 튜에서 값 추출---")
    tmp_value = refine_data[0]
    arranged_data = refine_data[1]
    print(tmp_value, arranged_data)
