def solution(prices):
    answer = []

    answer = prices[:]
    length = len(prices)

    if length < 2 or length > 100000:
        return
    else:
        for i in range(length):
            if prices[i] < 1 or prices[i] > 10000:
                return
            count = 0
            for j in prices[i + 1:]:
                count += 1
                if prices[i] > j:
                    answer[i] = count
                    break
            answer[i] = count
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))