def solution(n, lost, reserve):
    # n : 전체 학생 수, lost : 도난당한 학생 번호 담긴 배열, reserve : 여벌 옷 있는 학생들
    temp = lost[:]

    for i in lost:
        if i in reserve:
            temp.remove(i)
            reserve.remove(i)

    lost = temp[:]
    lost.sort()
    for i in lost:
        if i - 1 in reserve:
            temp.remove(i)
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            temp.remove(i)
            reserve.remove(i + 1)

    answer = n - len(temp)

    return answer


print(solution(5, [2, 4], [1, 3, 5]))
print()
print(solution(5, [2, 4], [3]))
print()
print(solution(3, [3], [1]))
print()
