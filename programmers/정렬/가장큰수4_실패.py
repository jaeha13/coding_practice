def gth(str1, str2):
    length1 = len(str1)
    length2 = len(str2)

    if length1 == length2:
        if str1 >= str2:
            return True
        return False

    i = 0
    while i < length1 and i < length2:
        if str1[i] > str2[i]:
            return True
        elif str1[i] < str2[i]:
            return False
        i += 1

    if i == length2:
        if str1[length2] >= str2[0]:
            return True
        return False
    elif i == length1:
        if str2[length1] >= str1[0]:
            return False
        return True


def solution(numbers):
    answer = ''

    c_numbers = []
    sorted_numbers = []
    length = len(numbers)
    temp = [0 for _ in range(length)]

    if temp == numbers:
        answer = '0'
        return answer

    for num in numbers:
        c_num = str(num)
        c_numbers.append(c_num)

    sorted_numbers.append(c_numbers[0])
    for k in range(1, length):
        flag = False
        for l in range(len(sorted_numbers)):
            if not gth(sorted_numbers[l], c_numbers[k]):
                sorted_numbers.insert(l, c_numbers[k])
                flag = True
                break
        if not flag:
            sorted_numbers.append(c_numbers[k])

    for num in sorted_numbers:
        answer += num

    return answer


print(solution([0]))     # 0
print()
print(solution([5]))     # 5
print()
print(solution([6, 10, 2]))     # 6210
print()
print(solution([3, 30, 34, 5, 9]))  # 9534330
print()
print(solution([3, 30, 31, 5, 9]))  # 9533130
print()
print(solution([3, 30, 31, 34, 9]))  # 93433130
print()
print(solution([909, 90, 908, 0, 0]))   # 9099090800
print()
print(solution([909, 90, 9, 0, 0]))   # 99099000