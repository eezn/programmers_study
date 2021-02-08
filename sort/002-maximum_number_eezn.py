# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.


numbers = [3, 30, 300, 94, 939, 9, 5, 0, 59]
# 9.94.939.59.5.3.30.300.0
# numbers = [3, 30, 300, 0, 0, 9, 5, 0, 59]


def compare_str(str1, str2):
    com1 = str1 + str2
    com2 = str2 + str1
    print(int(com1), "-", int(com2))
    print(int(com1) - int(com2))
    return int(com1) - int(com2)


def solution(numbers):
    answer = ''

    lst = []
    sorted_lst = []
    for elem in numbers:
        lst.append(str(elem).ljust(4, '#'))
    for elem in sorted(lst, reverse=True):
        sorted_lst.append(elem.rstrip('#'))
    print(sorted_lst)
    for i in range(len(sorted_lst)):
        print(sorted_lst)
        for j in range(i + 1, len(sorted_lst)):
            if compare_str(sorted_lst[i], sorted_lst[j]) < 0:
                tmp = sorted_lst[i]
                sorted_lst[i] = sorted_lst[j]
                sorted_lst[j] = tmp
                break
    print(sorted_lst)

    return answer


if __name__ == "__main__":
    solution(numbers)
