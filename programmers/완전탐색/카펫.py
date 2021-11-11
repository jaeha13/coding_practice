def solution(brown, yellow):
    answer = []
    lst = []

    for i in range(yellow):
        if yellow % (i + 1) == 0:
            lst.append(i + 1)

    length = len(lst)
    lst.sort(reverse=True)

    for j in range(length//2 + 1):
        if lst[j] * 2 + lst[length - 1 - j] * 2 + 4 == brown:
            answer.append(lst[j] + 2)
            answer.append(lst[length - 1 - j] + 2)
            break

    return answer


print(solution(10, 2))
print()
print(solution(8, 1))
print()
print(solution(24, 24))