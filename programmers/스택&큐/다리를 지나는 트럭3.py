"""deque : 스택과 큐 동시 사용 가능"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)   # bridge 만들기

    sum_t = 0
    while bridge:
        answer += 1
        w = bridge.popleft()
        sum_t -= w
        if truck_weights:
            if sum_t + truck_weights[0] <= weight:
                sum_t += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(2, 10, [8, 3, 2, 4, 9, 4]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))