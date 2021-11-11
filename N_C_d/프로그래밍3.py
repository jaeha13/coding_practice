def solution(v, a, b):  # v : 처음 연료량, a : 선두 시간당 소비량, b : 후위 시간당 소비량
    answer = 0

    flag = True
    while flag:
        v.sort(reverse=True)
        if v[0] < a:
            break
        for i in range(1, len(v)):
            if v[i] < b:
                flag = False
                break
        v[0] -= a
        v[1:] = map(lambda x: x - b, v[1:])
        answer += 1

    return answer


print(solution([4, 5, 5], 2, 1))
print()
print(solution([4, 4, 3], 2, 1))