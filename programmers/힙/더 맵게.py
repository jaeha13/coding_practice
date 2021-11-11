import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    a = heapq.heappop(scoville)

    while a < K and len(scoville) > 1:
        b = heapq.heappop(scoville)
        new = a + 2 * b
        heapq.heappush(scoville, new)
        answer += 1
        a = heapq.heappop(scoville)

    if a >= K:
        return answer
    elif len(scoville) == 1:
        if a + 2 * heapq.heappop(scoville) >= K:
            return answer + 1
    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
print()
print(solution([0, 0, 0, 1], 7))
print()
print(solution([1, 2, 3], 11)) # 1 + 2 * 2 => [5, 3] => 3 + 2 * 5 => 13