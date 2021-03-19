## 출처 Do it 자료구조와 함께 배우는 알고리즘 입문 - 파이썬
# pl -> start
# pt -> last
# pivot -> 자체 제작한 median of three 사용

from typing import MutableSequence


def quick_sort(data_array: MutableSequence, start: int, last: int) -> None:
    low = start
    high = last
    pivot = data_array[(start + last) // 2]

    print(f'data[{start}] ~ data[{last}]: ', *data_array[start: last + 1])  # 새로 추가된 부분

    while low <= high:
        while data_array[low] < pivot: low += 1
        while data_array[high] > pivot: high -= 1
        if low <= high:
            data_array[low], data_array[high] = data_array[high], data_array[low]
            low += 1
            high -= 1

    if start < high: quick_sort(data_array, start, high)
    if last > low: quick_sort(data_array, low, last)
    return data_array


if __name__ == '__main__':
    data = [4, 2, 5, 7, 9, 1, 3, 8, 6, 0]
    data = [13, 77, 49, 35, 61, 48, 73, 23, 95, 3, 89, 37, 57, 99, 17, 32, 94, 28, 15, 55, 7, 51, 88, 97, 62]
    last = int(len(data) - 1)
    print('{0}'.format(quick_sort(data, 0, last)))
