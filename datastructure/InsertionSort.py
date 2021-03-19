## K-MOOC 자료구조 강의 C++ 컨버전

def insertion_sort(data):
    n = len(data)

    for i in range(1, n):
        temp_data = data[i]
        for j in reversed(range(1, i + 1)):
            if data[j - 1] > temp_data:
                data[j] = data[j - 1]
            else:
                data[j] = temp_data
                break

        if data[0] > temp_data:
            data[0] = temp_data

    return data


def insertion_sort_range(data, start, last):
    # data[start], data[last] = data[last], data[start]

    for i in range(start, last + 1):
        temp_data = data[i]
        for j in reversed(range(1, i + 1)):
            if data[j - 1] > temp_data:
                data[j] = data[j - 1]
            else:
                data[j] = temp_data
                break

        if data[0] > temp_data:
            data[0] = temp_data

    return data


if __name__ == '__main__':
    data = [2, 4, 3, 1, 9, 6]
    print('{0}'.format(insertion_sort(data)))
