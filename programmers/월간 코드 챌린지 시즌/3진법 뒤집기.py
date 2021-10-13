from collections import deque


def solution(n):
    answer = 0

    que = deque()
    div = n
    while div > 0:
        mod = div % 3
        div = div // 3
        que.append(mod)

    que.reverse()
    for i in range(len(que)):
        answer += que[i] * (3 ** i)

    return answer


print(solution(45))