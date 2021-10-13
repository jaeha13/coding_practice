def solution(numbers):
    answer = []

    s = set()

    for i in range(len(numbers)):
        for n in numbers[i + 1:]:
            s.add(numbers[i] + n)

    for j in s:
        answer.append(j)
    answer.sort()

    return answer


print(solution([2, 1, 3, 4, 1]))
print()
print(solution([5, 0, 2, 7]))