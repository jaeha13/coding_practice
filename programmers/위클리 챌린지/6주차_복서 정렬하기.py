from collections import Counter, deque


def solution(weights, head2head):
    answer = []
    d = dict()

    for i, h in enumerate(head2head):
        win = Counter(h)
        d[i + 1] = win['W'] * 0.4

    print(d)



    return answer


print(solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]))
print()
print(solution([145, 92, 86], ["NLW", "WNL", "LWN"]))
print()
print(solution([60, 70, 60], ["NNN", "NNN", "NNN"]))