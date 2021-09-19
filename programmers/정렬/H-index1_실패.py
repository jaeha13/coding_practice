def solution(citations):
    answer = 0

    citations.sort()
    for i in range(len(citations)):
        if citations[i] <= len(citations[i:]):
            answer = citations[i]
        else:
            break

    return answer


print(solution([3, 0, 6, 1, 5]))
print()
print(solution([2, 4, 6, 1, 6]))
print()
print(solution([1, 1, 1, 1, 1]))
print()
print(solution([1, 1, 32, 1, 0]))