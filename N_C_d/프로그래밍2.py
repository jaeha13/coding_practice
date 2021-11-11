def print_g(graph):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            print(graph[i][j], end='\t')
        print()


def solution(costs, xcost, ycost):
    n, m = len(costs), len(costs[0])
    d = [[0] * m for _ in range(n)]

    dx = [1, 0] # 하단    비용 ycost
    dy = [0, 1] # 우측    비용 xcost
    d[0][0] = costs[0][0]

    def calculate(x, y):
        if x >= n or y >= m:
            return

        for k in range(len(dx)):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= n or ny >= m:
                continue
            if costs[nx][ny] - dx[k]*ycost - dy[k]*xcost >= 0:
                d[nx][ny] = d[x][y] + costs[nx][ny] - (dx[k]*ycost + dy[k]*xcost)
                return calculate(nx, ny)

    calculate(0, 0)
    print_g(d)
    answer = max(d[n - 1])
    return answer


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 1]], 0, 0))
print()
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print()
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 100, 0))
