from collections import Counter


def print_g(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j], end='\t')
        print()


def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])
    d = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != '.':
                d[i][j] = 1

    visited = [[False] * m for _ in range(n)]

    dx = [0, 0, -1, 1]  # 상하
    dy = [-1, 1, 0, 0]  # 좌우

    result = []
    lst = list()

    def check(x, y):
        if visited[x][y]:
            return
        if x < 0 or x >= n or y < 0 or y >= m:
            return
        if d[x][y] == 0:
            return
        visited[x][y] = True
        lst.append(maps[x][y])

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if d[nx][ny] == 0:
                continue
            d[x][y] = 0
            if not visited[nx][ny]:
                check(nx, ny)

        return lst

    for i in range(n):
        for j in range(m):
            if d[i][j] == 0:
                continue
            n_lst = check(i, j)
            result.append(n_lst)
            lst = []

    for i, l in enumerate(result):
        if l is not None:
            di = dict(Counter(l))
            nn_lst = [k for k, v in di.items() if v == max(di.values())]
            nn_lst.sort(reverse=True)
            for j in range(len(l)):
                if l[j] not in nn_lst:
                    l[j] = nn_lst[0]

    dic = dict()
    for i in range(65, 91):
        dic[chr(i)] = 0

    for i in range(len(result)):
        if result[i] is None:
            continue
        for j in range(len(result[i])):
            dic[result[i][j]] += 1

    answer = max(dic.values())

    return answer


print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))
print()
print(solution(["XY..", "YX..", "..YX", ".AXY"]))