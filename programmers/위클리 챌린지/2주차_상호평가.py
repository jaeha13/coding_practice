def solution(scores):
    answer = ''
    max_s = []
    min_s = []
    lst_s = []
    for i in range(len(scores)):
        max_score = 0
        min_score = 100
        max_c = 1
        min_c = 1
        for j in range(len(scores[i])):
            if max_score < scores[j][i]:
                max_score = scores[j][i]
            elif max_score == scores[j][i]:
                max_c += 1
            elif min_score > scores[j][i]:
                min_score = scores[j][i]
            elif min_score == scores[j][i]:
                min_c += 1
        max_s.append(max_score ** max_c)
        min_s.append(min_score ** min_c)

    for i in range(len(scores)):
        sum_s = 0
        n = len(scores)
        for j in range(len(scores[i])):
            if i == j and scores[i][j] in [max_s[i], min_s[i]]:
                n -= 1
                continue
            sum_s += scores[j][i]
        lst_s.append(sum_s / n)

    for s in lst_s:
        if s >= 90:
            answer += 'A'
        elif s >= 80:
            answer += 'B'
        elif s >= 70:
            answer += 'C'
        elif s >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
print()
print(solution([[50, 90], [50, 87]]))
print()
print(solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]))