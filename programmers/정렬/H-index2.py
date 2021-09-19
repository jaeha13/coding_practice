def solution(citations):
    answer = 0

    citations.sort()
    length = len(citations)
    for i in range(length):
        if citations[i] <= length - i:
            answer = citations[i]
        else:
            if answer < length - i:
                answer = length - i
            break

    return answer


print(solution([3, 0, 6, 1, 5]))    # 3
print()
print(solution([2, 4, 6, 1, 6]))    # 3
print()
print(solution([1, 1, 1, 1, 1]))    # 1
print()
print(solution([1, 1, 32, 1, 0]))   # 1