def solution(progresses, speeds):
    answer = []

    while True:
        length = len(progresses)
        count = 0
        if length == 0:
            break
        day = 100 - progresses[0]
        for i in range(length):
            progresses[i] += (day * speeds[i])
            if progresses[i] >= 100:
                count += 1
            else:
                break
        answer.append(count)
        j = 0
        while j < count:
            j += 1
            progresses.pop(0)
            speeds.pop(0)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print()
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))