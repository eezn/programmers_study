from typing import MutableSequence

from datastructure import Heapify


## (k-1)/2
## 2k +1
## 2K +2

def heap_sort(data_array: MutableSequence):
    n = len(data_array)

    print('주어진 자료')
    for ele in enumerate(data_array):
        print(ele, end=' ')
    print('\n\n')
    # data_array[i] ~ data_array[i-1]을 heapify하기
    for i in range((n - 1) // 2, -1, -1):  # 배열의 중간(leaf node)에서 0까지
        Heapify.percolation_down(data_array, i, n - 1)

    # data_array[0] (최대값)과 마지막 원소를 교환
    # data_array[i] ~ data_array[i-1]을 heapify하기
    for i in range(n - 1, 0, -1):  # n-1에서 1까지
        print('가장 큰 원소인 {0}와 마지막 원소 {1}를 교환.'.format(data_array[0], data_array[-1]))
        data_array[0], data_array[i] = data_array[i], data_array[0]
        for ele in enumerate(data_array):
            print(ele, end=' ')
        print(' ')
        Heapify.percolation_down(data_array, 0, i - 1)
    return data_array


if __name__ == '__main__':
    data = [4, 2, 5, 7, 9, 1, 3, 8, 6, 0]
    # data = [4, 21, 33, 42, 65, 2, 5, 7, 9, 1, 3, 8, 6, 0]
    # data = [13, 77, 49, 35, 61, 48, 73, 23, 95, 89, 37, 57, 99, 17, 32, 94, 28, 15, 55, 17, 51, 88, 97, 62]
    # data = [13, 77, 49, 35, 61, 48, 73, 15, 55, 11, 51, 88, 97, 62]
    # data = [13, 77, 49, 35, 11, 51, 88, 97]
    print('최종 heap 정렬 된 배열 \n{0}'.format(heap_sort(data)))
