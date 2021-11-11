def solution(info): # info [A, B]: A=시작시간, B=종료시간 초단위
    n = len(info)
    d = dict()
    info.sort(key=lambda x: x[1], reverse=True)
    max_h = info[0][1]
    info.sort(key=lambda x: x[0])
    min_h = info[0][0]

    for i in range(min_h, max_h + 1):
        d[str(i)] = 0
    for i in range(n):
        for j in range(info[i][0], info[i][1] + 1):
            d[str(j)] += 1

    answer = [k for k, v in d.items() if max(d.values()) == v]

    return answer


print(solution([[1, 5], [3, 5], [7, 8]]))
print()
print(solution([[2, 3], [2, 5], [2, 2], [3, 3]]))
print()
print(solution([[1, 2], [2, 3], [4, 5], [5, 6]]))