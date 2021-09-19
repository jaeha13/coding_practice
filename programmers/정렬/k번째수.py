def solution(array, commands):
    answer = []

    for lst in commands:
        sorted_lst = array[lst[0] - 1:lst[1]]
        sorted_lst.sort()
        data = sorted_lst[lst[2] - 1]
        answer.append(data)

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))