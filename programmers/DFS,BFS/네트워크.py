def solution(n, computers):
    answer = 0
    visited = set()     # 중복 허용 x

    def check(computers_, start, visited_):
        if start in visited_:   # 방문한 적이 있어?? --> 이미 확인 끝! 다른 link 가 아니야
            return 0

        visited_.add(start)
        for i in range(n):
            if i == start or computers_[start][i] == 0:     # 자기 자신이거나 연결이 안되어 있으면
                continue    # 다음
            if i not in visited_:   # 연결되어있는데 visited_에 없으면
                check(computers_, i, visited_)   # 탐색
        return 1    # 새로운 경로 발견

    for idx in range(n):
        answer += check(computers, idx, visited)    # 연결 됐으면 1, 아니면 0
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print()
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))