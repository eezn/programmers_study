#
p1 = ["leo", "kiki", "eden"]
c1 = ["eden", "kiki"]

p2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
c2 = ["josipa", "filipa", "marina", "nikola"]

p3 = ["mislav", "stanko", "mislav", "ana"]
c3 = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant.sort()
    # print(participant)
    completion.sort()
    # print(completion)
    r = None
    for p, c in zip(participant, completion):
        if p != c:
            return p
    if r is None:
        r = participant[-1]
    return r


if __name__ == '__main__':
    print(solution(p1, c1))
