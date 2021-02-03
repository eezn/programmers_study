#
#

def solution1(array, commands):
    answer = []
    for i, j, k in commands:
        split_array = array[i - 1:j]
        print(split_array)
        split_array.sort()
        print(split_array[k - 1])
        answer.append(split_array[k - 1])
    return answer


if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    print(solution1(array, commands))
