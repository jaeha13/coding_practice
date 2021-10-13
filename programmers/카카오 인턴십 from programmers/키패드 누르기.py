keypad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          ['*', 0, '#']]


def solution(numbers, hand):
    answer = ''

    r_pos = [[3, 2]]
    l_pos = [[3, 0]]

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            row = num // 3
            col = num % 3 - 1
            if col == -1:
                col = 2
            l_pos.append([row, col])
        elif num in [3, 6, 9]:
            answer += 'R'
            row = num // 3 - 1
            col = num % 3 - 1
            if col == -1:
                col = 2
            r_pos.append([row, col])
        else:
            if num == 0:
                temp = 11
            else:
                temp = num
            r_n = r_pos[-1]
            l_n = l_pos[-1]
            row = temp // 3
            col = temp % 3 - 1
            if col == -1:
                col = 2
            pos = [row, col]
            r_count = abs(r_n[0] - pos[0]) + abs(r_n[1] - pos[1])
            l_count = abs(l_n[0] - pos[0]) + abs(l_n[1] - pos[1])
            if r_count > l_count:
                answer += 'L'
                l_pos.append(pos)
            elif r_count < l_count:
                answer += 'R'
                r_pos.append(pos)
            elif hand == 'left':
                answer += 'L'
                l_pos.append(pos)
            else:
                answer += 'R'
                r_pos.append(pos)
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print()
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print()
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))