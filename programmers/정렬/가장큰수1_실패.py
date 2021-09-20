def solution(numbers):
    answer = ''

    c_numbers = []
    length = len(numbers)

    for num in numbers:
        c_num = str(num)
        c_numbers.append(c_num)
    c_numbers.sort(reverse=True)

    i = 0
    while i < length:
        subset = []
        for j in range(i + 1, length):
            if c_numbers[i][0] != c_numbers[j][0]:
                break
            if j == i + 1:
                subset.append(c_numbers[i])
            subset.append(c_numbers[j])
        if not subset:
            i += 1
            continue
        for k in range(len(subset)):
            subset[k] = subset[k][len(subset[k]) - 1::-1]
        subset.sort(reverse=True)
        for l in range(len(subset)):
            subset[l] = subset[l][len(subset[l]) - 1::-1]
        c_numbers[i:i + len(subset)] = subset[:]
        i = i + len(subset)
    for num in c_numbers:
        answer += num
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
print()
print(solution([0, 0, 0, 0, 0]))
print()
print(solution([21, 212]))