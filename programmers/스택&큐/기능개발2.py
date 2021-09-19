def solution(progresses, speeds):
    answer = []

    while True:
        length = len(progresses)
        if length == 0:
            break
        count = 0
        day = (100 - progresses[0])//speeds[0]
        if (100 - progresses[0]) % speeds[0] > 0:
            day += 1
        for i in range(length):
            progresses[i] += (day * speeds[i])
        for j in range(length):
            if progresses[j] >= 100:
                count += 1
            else:
                break
        for _ in range(count):
            progresses.pop(0)
            speeds.pop(0)
        answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print()
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print()
print(solution([95, 90, 99, 99, 80, 99], [5, 3, 7, 1, 1, 1]))
print()
print(solution([95, 90, 99, 99, 80, 99], [4, 3, 7, 1, 1, 1]))