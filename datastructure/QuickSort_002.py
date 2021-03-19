## 출처 Do it 자료구조와 함께 배우는 알고리즘 입문 - 파이썬
# pl -> start
# pt -> last
# pivot -> 자체 제작한 median of three 사용

from typing import MutableSequence

from datastructure import MedianOfThree, InsertionSort


def quick_sort(data_array: MutableSequence, start: int, last: int) -> None:
    low = start
    high = last
    NUM_THRESHOLD = 3
    print('주어진 데이터: {0}'.format(data_array))
    pivot = MedianOfThree.find_pivot_index(data_array, low, (low + high) // 2, high)
    # pivot = data_array[(start + last) // 2]
    print('MoT 정렬 후: {0}, pivot: {1}'.format(data_array, pivot))
    if (last - start < NUM_THRESHOLD):
        InsertionSort.insertion_sort(data_array)
        print('{0}보다 작은 배열로 삽입 정렬 후: {1}'.format(NUM_THRESHOLD, data_array))
        print("-------------------")
        return data_array
    print(f'index[{start}] ~ [{last}]: ', *data_array[start: last + 1])  # 새로 추가된 부분

    while low <= high:
        while data_array[low] < pivot:
            # if low >= len(data_array): break
            low += 1

        while data_array[high] > pivot:
            # if high < 1: break
            high -= 1

        if low <= high:
            data_array[low], data_array[high] = data_array[high], data_array[low]
            # if low >= len(data_array):
            low += 1
            # else:
            #     low = len(data_array) - 1
            # if high < 1:
            #     high = 0
            # else:
            high -= 1
    print("-------------------")
    if start < high: quick_sort(data_array, start, high)
    if last > low: quick_sort(data_array, low, last)
    return data_array


if __name__ == '__main__':
    # data = [4, 2, 5, 7, 9, 1, 3, 8, 6, 0]
    # data = [4, 21, 33, 42, 65, 2, 5, 7, 9, 1, 3, 8, 6, 0]
    # data = [13, 77, 49, 35, 61, 48, 73, 23, 95, 89, 37, 57, 99, 17, 32, 94, 28, 15, 55, 7, 51, 88, 97, 62]
    data = [13, 77, 49, 35, 61, 48, 73, 15, 55, 7, 51, 88, 97, 62]
    # data = [13, 77, 49, 35, 7, 51, 88, 97]
    last = int(len(data) - 1)
    print('{0}'.format(quick_sort(data, 0, last)))
