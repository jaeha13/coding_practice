from collections import deque


def solution(priorities, location):
    answer = 0

    length = len(priorities)

    wait = deque([priorities[i] for i in range(length)])

    if length < 1 or length > 100:
        return

    # 대기열에 입력
    index = 0
    prior = priorities[location]
    while True:
        max_p = max(wait)
        if max_p == prior and index == location:
            answer += 1
            break
        if max_p == wait[0]:
            answer += 1
            wait.popleft()
        else:
            wait.append(wait.popleft())
        index = (index + 1) % length

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))