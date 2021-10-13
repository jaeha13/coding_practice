def solution(price, money, count):
    answer = 0

    need = 0

    for i in range(1, count + 1):
        need += price * i

    answer += (need - money)
    if answer <= 0:
        return 0

    return answer


print(solution(3, 20, 4))