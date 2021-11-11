from itertools import product


def solution(word):
    answer = 0

    vow = ['A', 'E', 'I', 'O', 'U']

    vow_dict = []
    for i in range(5):
        string = list(product(vow, repeat=i + 1))
        for j in string:
            st = ''.join(j)
            vow_dict.append(st)

    vow_dict.sort()
    for i, w in enumerate(vow_dict):
        print(i, w)
        if word == w:
            answer += i + 1
            break

    return answer


print(solution('AAAAE'))
print()
print(solution('AAAE'))
print()
print(solution('I'))
print()
print(solution('EIO'))