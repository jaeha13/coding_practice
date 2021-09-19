def solution(priorities, location):
    answer = 0

    length = len(priorities)

    if length < 1 or length > 100:
        return
    if location < 0 or location >= length:
        return

    prior = priorities[location]

    wait = priorities[:]
    priorities.sort(reverse=True)

    if priorities[0] > 9 or priorities[length - 1] < 1:
        return

    while wait:
        if wait[0] == priorities[0]:  # 대기번호 0번이 우선순위가 가장 높은 것
            if prior == priorities[0] and location == 0:  # 뽑고자 하는 문서인 경우
                answer += 1
                break
            wait.pop(0)
            priorities.pop(0)
            answer += 1
            length -= 1
        else:
            wait.append(wait.pop(0))
        location = (location - 1) % length

    return answer


print(solution([2, 1, 3, 2], 2))
print()
print(solution([1, 1, 9, 1, 1, 1], 0))
print()
print(solution([1, 1, 1, 1, 1, 1], 4))
print()
print(solution([1, 2, 8, 3, 4], 4))
print()
print(solution([1, 2, 8, 3, 4], 3))
print()
print(solution([3], 0))