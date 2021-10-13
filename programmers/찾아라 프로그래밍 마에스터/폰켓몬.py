from collections import Counter


def solution(nums):
    answer = 0

    count = Counter(nums)
    length = len(count.keys())
    num = len(nums)
    if num // 2 < length:
        answer += num // 2
    else:
        answer += length

    return answer


print(solution([3, 1, 2, 3]))
print()
print(solution([3, 3, 3, 2, 2, 4]))
print()
print(solution([3, 3, 3, 2, 2, 2]))
