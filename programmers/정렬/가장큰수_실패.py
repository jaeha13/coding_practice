def solution(numbers):
    answer = ''

    rev_num = []
    for num in numbers:
        c_num = str(num)
        c_num = c_num[len(c_num) - 1:: -1]
        rev_num.append(c_num)
    rev_num.sort(reverse=True)
    for c in rev_num:
        answer += c[len(c) - 1:: -1]

    return answer


print(solution([6, 10, 2])) # 6210
print()
print(solution([3, 30, 34, 5, 9]))  # 9534330
print()
print(solution([3, 30, 31, 5, 9]))  # 9533130
print()
print(solution([3, 30, 31, 34, 9]))  # 93433130
print()
print(solution([23, 30, 34, 13, 9]))    # 934302313