def generate_lst(lst):
    length = len(lst)

    for i in range(length):
        temp = lst[:]
        del temp[i]
        for n2 in temp:
            if len(lst[i] + n2) > length:
                return
            if str(int(lst[i] + n2)) not in lst:
                lst.append(lst[i] + n2)


def is_prime(num):
    if num == 1 or num == 0:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    lst = []

    for num in numbers:
        lst.append(num)

    generate_lst(lst)
    for i in range(len(lst)):
        re_num = lst[i][len(lst[i])::-1]
        if str(int(re_num)) not in lst:
            lst.append(re_num)

    print(lst)
    for num in lst:
        if is_prime(int(num)):
            print(num)
            answer += 1

    return answer


print(solution("17"))
print()
print(solution("011"))