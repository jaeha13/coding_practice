def solution(numbers):
    answer = 0

    for i in range(10):
        if i not in numbers:
            answer += i

    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print()
print(solution([5, 8, 4, 0, 6, 7, 9]))