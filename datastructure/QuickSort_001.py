## K-MOOC 자료구조 강의 C++ 컨버전
## median 값을 구해야하는 find_pivot()까지 구현하다가 관둠..

import MedianOfThree as mot
from datastructure.InsertionSort import insertion_sort

count = 0


def quick_sort(data, first, last):
    global count
    NUM_THRESHOLD = 6
    # first = 0
    # last = len(data)
    print("===들어온 데이터===")
    # data = data[first:last]
    print('앞 인덱스 포인터: {0} , 뒤 인덱스 포인: {1}, 자료: {2}'.format(first, last, data))
    if (last - first) < NUM_THRESHOLD:
        print("===삽입정렬===")
        insertion_sort(data[first:last])
        print('삽입 정렬된 데이터: {0}'.format(data))
    elif (last - first) <= 1:
        return data
    else:
        # pivot = find_pivot(data, first, last)
        arraged_array = mot.find_pivot(data)
        pivot = arraged_array[0]
        # data = arraged_array[1]

        low = first + 1;
        high = last - 2
        while data[low] < pivot:
            low += 1
        while data[high] > pivot:
            high -= 1
        while low < high:
            data[low], data[high] = data[high], data[low]
            low += 1
            high -= 1
            while data[low] < pivot:
                low += 1
            while data[high] > pivot:
                high -= 1

        print('현재 앞 인덱스 포인터: {0}, 현재 마지막 인덱스 포인터: {1}, 현재 피봇: {2}'.format(first, last, pivot))
        # data[last - 1] = copy.deepcopy(data[low])
        # data[low] = copy.deepcopy(pivot)
        data[last - 1] = data[low]
        data[low] = pivot
        # count += 1
        # print(count)
        # pre_data = data[first:low]
        # post_data = data[high:last]
        quick_sort(data, first, low)
        quick_sort(data, high, last)
    return data


if __name__ == '__main__':
    data = [4, 2, 5, 7, 9, 1, 3, 8, 6, 0]
    # data = [13, 77, 49, 35, 61, 48, 73, 23, 95, 3, 89, 37, 57, 99, 17, 32, 94, 28, 15, 55, 7, 51, 88, 97, 62]
    last = len(data)
    print('{0}'.format(quick_sort(data, 0, last)))
