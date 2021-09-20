def solution(answers):
    answer = []

    length = len(answers)

    a, b, c = [0 for _ in range(length)], [0 for _ in range(length)], [0 for _ in range(length)]
    for i in range(length):
        a[i] = (i % 5) + 1
        if i % 2 == 0:
            b[i] = 2
        elif i % 8 == 1:
            b[i] = 1
        elif i % 8 == 3:
            b[i] = 3
        elif i % 8 == 5:
            b[i] = 4
        elif i % 8 == 7:
            b[i] = 5

    i = 0
    while i <= length - 1:
        if i % 10 == 0:
            c[i] = 3
        elif i % 10 == 2:
            c[i] = 1
        elif i % 10 == 4:
            c[i] = 2
        elif i % 10 == 6:
            c[i] = 4
        else:
            c[i] = 5
        if i + 1 <= length - 1:
            c[i + 1] = c[i]
        i += 2

    j = 0
    count1, count2, count3 = 0, 0, 0
    while j < length:
        if answers[j] == a[j]:
            count1 += 1
        if answers[j] == b[j]:
            count2 += 1
        if answers[j] == c[j]:
            count3 += 1
        j += 1

    max_count = max(count1, count2, count3)

    if max_count == count1:
        answer.append(1)
    if max_count == count2:
        answer.append(2)
    if max_count == count3:
        answer.append(3)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))