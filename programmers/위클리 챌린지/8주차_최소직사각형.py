def solution(sizes):
    answer = 0

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:  # 뒤 쪽 값이 크게
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

    w = []
    h = []
    for s in sizes:
        w.append(s[0])
        h.append(s[1])

    m_w = max(w)
    m_h = max(h)

    answer += m_w * m_h

    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print()
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print()
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))