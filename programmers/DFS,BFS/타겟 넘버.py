def solution(numbers, target):
    answer = 0

    def dfs(num, level):
        nonlocal answer

        if level == len(numbers) - 1:
            if num == target:
                answer += 1
            return

        if not level:
            dfs(-num + numbers[level], level + 1)
            dfs(-num - numbers[level], level + 1)
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(numbers[0], 0)
    return answer


print(solution([1, 1, 1, 1, 1],	3))