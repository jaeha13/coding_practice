def solution(bridge_length, weight, truck_weights):
    answer = 0
    length = len(truck_weights)

    if bridge_length < 1 or bridge_length > 10000:
        return
    if weight < 1 or weight > 10000:
        return
    if length < 1 or length > 10000:
        return
    i = 0
    while i < length:
        if truck_weights[i] < 1 or truck_weights[i] > weight:
            return
        if i == length - 1:
            answer += bridge_length
            break
        sum = truck_weights[i]
        count = 1
        while count < bridge_length:
            sum += truck_weights[i + count]
            if sum > weight:
                break
            count += 1
            if sum == weight:
                break
        answer += bridge_length + (count - 1)
        i += count
    answer += 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(2, 10, [8, 3, 2, 4, 9, 4]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))