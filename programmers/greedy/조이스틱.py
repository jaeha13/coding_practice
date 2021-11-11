def solution(name):
    answer = 0
    length = len(name)

    arr = [x for x in range(length) if name[x] != 'A']  # 'A' 가 아닌 경우

    arr2 = [(x - length) for x in range(length) if name[x] != 'A']
    #   [-length, -length + 1, -length + 2, -length + 3, ...., -1]
    arr2.sort(reverse=True)
    pre = [ord(name[x]) - ord('A') for x in arr]
    post = [abs(ord(name[x]) - ord('Z')) + 1 for x in arr]

    print(arr)
    print(arr2)
    print(pre)
    print(post)

    current = 0
    for i in range(len(arr)):
        print(current)
        print('뒤쪽 부터', (arr[i] - current) > abs(current - abs(arr2[i])))
        if (arr[i] - current) > abs(current - abs(arr2[i])):
            print(abs(current - abs(arr2[i])))
            answer += (current - abs(arr2[i]))
            answer += min(pre[len(arr) - i - 1], post[len(arr) - i - 1])
            print(min(pre[len(arr) - i - 1], post[len(arr) - i - 1]))
            current = length - abs(arr2[i])
        else:
            answer += (arr[i] - current)
            print((arr[i] - current))
            answer += min(pre[i], post[i])
            print(min(pre[i], post[i]))
            current = arr[i]
        print(current)
    return answer


print(solution("JEROEN"))
print()
print(solution("JAN"))
