## K-MOOC 자료구조 강의 C++ 컨버전
## median 값을 구해야하는 find_pivot()까지 구현하다가 관둠..

from datastructure.InsertionSort import insertion_sort


def find_pivot(data, first, last):
    print(data[first], data[len(data) // 2], data[last - 1])


def quick_sort(data, first, last):
    NUM_THRESHOLD = 6
    if (last - first) < NUM_THRESHOLD:
        insertion_sort(data[first:])
    else:
        pivot = find_pivot(data, first, last)
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
        data[last - 1] = data[low]
        data[low] = pivot
        quick_sort(data, first, low)
        quick_sort(data, high, last)
    return data


if __name__ == '__main__':
    data = [4, 2, 5, 7, 9, 1, 3, 8, 6, 0]
    data = [13, 77, 49, 35, 61, 48, 73, 23, 95, 3, 89, 37, 57, 99, 17, 32, 94, 28, 15, 55, 7, 51, 88, 97, 62]
    last = len(data)
    print('{0}'.format(quick_sort(data, 0, last)))
