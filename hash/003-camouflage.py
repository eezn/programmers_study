##
#

c1_t = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

c1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
c2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]



def solution(clothes):
    a = 0
    set_data = set()
    for i in clothes:
        # print(i[0])
        set_data.add(i[0])
        a += 1
        for j in clothes:
            t1 = i[0] + "+" + j[0]
            t2 = j[0] + "+" + i[0]
            # print(t1, t2)
            if i[1] == j[1]:
                continue
            if t1 == t2:
                continue
            if t1 not in set_data and t2 not in set_data:
                set_data.add(t1)
                # print(t1)
                a += 1
    # print(set_data)
    # print(a)
    return a


c1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution_use_dict(clothes):
    attribute = dict()
    for v in clothes:
        v
    for value, key in clothes:
        if attribute.get(key) is None:
            attribute[key] = []
            attribute[key].append(value)
        else:
            attribute[key].append(value)
    # print(attribute)
    count = 0

    set_attribute = set()
    keys = list(attribute.keys())

    keys = iter(list(attribute.keys()))
    # print(keys)
    #
    while True:
        try:
            current_pointer = next(keys)
            print(current_pointer)
            next_pointer = next(keys)
            print(next_pointer)

        except StopIteration:
            break

    print(count)
    answer = 0
    return answer

def solution_use_dict2(clothes):
    attribute = dict()
    for value, key in clothes:
        if attribute.get(key) is None:
            attribute[key] = []
            attribute[key].append(value)
        else:
            attribute[key].append(value)
    print(attribute)
    count = 0
    keys_list = list(attribute.keys())
    print(len(keys_list))

    value_list = []
    for key in keys_list:
        print(attribute.get(key))
        count += len(attribute.get(key))
        for value in attribute.get(key):
            value_list.append(value)
    # dataSet = value_list
    print(count)
    print(value_list)
    # mCand = []
    # for i in range(len(dataSet)):
    #     for j in range(i+1, len(dataSet)):
    #         set1 = set(dataSet[i]).union(set(dataSet[j])) #중복 부분집합 합치기
    #         if len(set1) > len(dataSet[i]) + 1:
    #             continue
    #         list1 = list(set1)
    #         list1.sort()	#부분집합을 정렬
    #         if tuple(list1) not in mCand:
    #             mCand.append(tuple(list1))
    # print(mCand)




if __name__ == '__main__':
    # solution(c1_t)
    print(solution_use_dict2(c1))
