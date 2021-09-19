def solution(prices):
    length = len(prices)
    answer = [0 for _ in range(length)]

    if length < 2 or length > 100000:
        return
    else:
        for i in range(length):
            if prices[i] < 1 or prices[i] > 10000:
                return
            count = 0
            for j in range(i + 1, length):
                count += 1
                if prices[i] > prices[j]:
                    answer[i] = count
                    break
            answer[i] = count
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))