import heapq


def solution(jobs):
    answer = 0

    heap = []
    for st, job in jobs:
        heapq.heappush(heap, (job, st))
    std = 0     # 전 작업 끝나는 시점
    result = 0
    for _ in range(len(jobs)):
        job, st = heapq.heappop(heap)
        time = (std - st + job) # 내 일을 끝내는데 총 걸린 시간
        result += time
        std += job

    answer += int(result / len(jobs))
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))