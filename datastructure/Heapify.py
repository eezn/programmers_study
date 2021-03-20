from typing import MutableSequence


def percolation_down(data_array: MutableSequence, left: int, right: int):
    temp = data_array[left]  # Root
    parent = left

    ## (k-1)/2
    ## 2k +1
    ## 2K +2

    while parent < (right + 1) // 2:
        child_left = parent * 2 + 1
        child_right = child_left + 1
        # child_right = parent * 2 + 2

        if child_right <= right and data_array[child_right] > data_array[child_left]:
            child = child_right
            print('Percolation down ->  부모index: {0}, 좌index: {1}, 우index: {2} -> 우-부모 변경'.
                  format(parent, child_left, child_right))
            for ele in enumerate(data_array):
                print(ele, end=' ')
            print(' ')
        else:
            child = child_left
            print('Percolation down ->  부모index: {0k, 좌index: {1}, 우index: {2} -> 좌-부모 변경'.
                  format(parent, child_left, child_right))
            for ele in enumerate(data_array):
                print(ele, end=' ')
            print(' ')

        if temp >= data_array[child]:
            break
        data_array[parent] = data_array[child]
        parent = child
    data_array[parent] = temp
    print('부모-자식 비교 후 변경 완료 혹은 유된 배열')
    for ele in enumerate(data_array):
        print(ele, end=' ')
    print(' ')
    print(' ')
    return data_array
