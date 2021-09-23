def solution(clothes):
    answer = 0

    cth_dict = dict()

    for cth in clothes:
        if cth[1] not in cth_dict:
            cth_dict[cth[1]] = 1
        else:
            cth_dict[cth[1]] += 1

    lst = []

    for item in cth_dict.values():
        lst.append(item)

    mul = 1
    for n in lst:
        mul *= (n + 1)
    answer += (mul - 1)    # 아무것도 안입은 경우 제외

    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print()
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))