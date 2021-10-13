from collections import deque


def solution(s):
    answer = 0

    que = deque(s)

    num_str = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

    str_num = {v: k for k, v in num_str.items()}

    i = 0
    string = ''
    lst = []
    while i < len(s):
        ch = que.popleft()
        string += ch
        if ch in [str(i) for i in range(10)]:
            lst.append(ch)
        else:
            while string not in str_num.keys():
                string += que.popleft()
                i += 1
            lst.append(str_num[string])
        i += 1
        string = ''

    answer += int(''.join(list(map(str, lst))))
    return answer


print(solution("one4seveneight"))
print()
print(solution("23four5six7"))
print()
print(solution("2three45sixseven"))
print()
print(solution("123"))