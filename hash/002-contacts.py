p1 = ["119", "97674223", "1195524421"]
p2 = ["123","456","789"]
p3 = ["12","123","1235","567","88"]


def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]:
            return False

    return True


if __name__ == '__main__':
    print(solution(p3))