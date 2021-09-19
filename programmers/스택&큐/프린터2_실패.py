from collections import deque


def solution(priorities, location):
    answer = 0

    length = len(priorities)
    prior = priorities[location]

    if length < 1 or length > 100:
        return
    if location < 0 or location >= length:
        return

    wait = deque(priorities[i] for i in range(length))
    priorities.sort(reverse=True)

    index = 0
    while wait:
        if wait[0] < 1 or wait[0] > 9:
            return
        if prior == priorities[0] and index == location:    # 뽑고자 하는 문서인 경우
            answer += 1
            break
        elif wait[0] == priorities[0]:  # 뽑고자 하는 문서는 아니지만 우선순위가 높은 것
            priorities.pop(0)
            wait.popleft()
            answer += 1
        else:
            wait.append(wait.popleft())
        index = (index + 1) % length
        print(wait, answer)

    return answer


print(solution([2, 1, 3, 2], 2))
print()
print(solution([1, 1, 9, 1, 1, 1], 0))