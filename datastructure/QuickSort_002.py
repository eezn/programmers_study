## 출처 Do it 자료구조와 함께 배우는 알고리즘 입문 - 파이썬
# pl -> start
# pt -> last
# pivot -> 자체 제작한 median of three 사용

from typing import MutableSequence


def quick_sort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x = a[(left - right) // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: quick_sort(a, left, pr)
    if right > pl: quick_sort(a, pl, right)


if __name__ == '__main__':
    data = [4, 2, 5, 7, 9, 1, 3, 8, 6, 0]
    # data = [13, 77, 49, 35, 61, 48, 73, 23, 95, 3, 89, 37, 57, 99, 17, 32, 94, 28, 15, 55, 7, 51, 88, 97, 62]
    last = int(len(data) - 1)
    print('{0}'.format(quick_sort(data, 0, last)))
