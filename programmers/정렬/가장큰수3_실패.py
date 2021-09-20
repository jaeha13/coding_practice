def gth(str1, str2):
    length1 = len(str1)
    length2 = len(str2)

    if length1 == length2:
        if str1 > str2:
            return True
        return False

    elif length1 > length2:
        i = 0
        while i < length2:
            if str1[i] > str2[i]:
                return True
            elif str1[i] < str2[i]:
                return False
            i += 1
        if str1[i] >= str2[0]:
            return True
        return False

    else:
        i = 0
        while i < length1:
            if str1[i] > str2[i]:
                return True
            elif str1[i] < str2[i]:
                return False
            i += 1
        if str2[i] >= str1[0]:
            return False
        return True


def solution(numbers):
    answer = ''

    c_numbers = []
    length = len(numbers)
    temp = [0 for _ in range(length)]

    if temp == numbers:
        answer = '0'
        return answer

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

        k = 0
        while k < len(subset) - 1:
            for l in range(k + 1, len(subset)):
                if not gth(subset[k], subset[l]):  # 뒤가 크면
                    subset[k], subset[l] = subset[l], subset[k]
                l += 1
            k += 1

        c_numbers[i:i + len(subset)] = subset[:]
        i = i + len(subset)

    for num in c_numbers:
        answer += num
    return answer


print(solution([6, 10, 2]))     # 6210
print()
print(solution([3, 30, 34, 5, 9]))  # 9534330
print()
print(solution([3, 30, 31, 5, 9]))  # 9533130
print()
print(solution([3, 30, 31, 34, 9]))  # 93433130
print()
print(solution([909, 90, 908, 0, 0]))   # 9099090800