def solution(citations):
    answer = 0

    citations.sort()
    for i in range(len(citations)):
        if answer <= len(citations[i:]):
            answer = citations[i]
        else:
            break

    return answer


print(solution([3, 0, 6, 1, 5]))