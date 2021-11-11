from collections import Counter

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

attack = []
for j in range(m):
    attack.append(list(map(int, input().split())))

blast_marble = []


# 0.1 board_printer()
def board_printer(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='\t')
        print()


# 0.2 array 채우기
def array_reset(lst, arr):
    direction_r = [0, 1, 0, -1]  # l, d, r, u
    direction_c = [-1, 0, 1, 0]
    x, y = int((n - 1) / 2), int((n - 1) / 2)
    k = 0
    for i in range(2, 2 * n, 2):  # l, d, r, r, u, u, l, l, l, d, d, d, r, r, r, r, u, u, u, u
        for j in range(2):
            for _ in range(i // 2):
                nx = x + direction_r[(i + j) % 4 - 2]
                ny = y + direction_c[(i + j) % 4 - 2]
                arr[x][y] = lst[k]
                x, y = nx, ny
                k += 1
    return lst


# 1. 얼음 공격
def blizard(arr, d, s):
    x, y = int((n - 1) / 2), int((n - 1) / 2)
    for k in range(s):
        if d == 1:  # 위
            nx = x - (k + 1)
            ny = y
        elif d == 2: # 아래
            nx = x + (k + 1)
            ny = y
        elif d == 3: # 좌
            nx = x
            ny = y - (k + 1)
        else:   # 우
            nx = x
            ny = y + (k + 1)
        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
            break
        arr[nx][ny] = 0


# 1-1. 구슬 이동
def move(arr, x, y): # x, y: center
    lst = []
    direction_r = [0, 1, 0, -1] # l, d, r, u
    direction_c = [-1, 0, 1, 0]
    for i in range(2, 2 * n, 2):  # l, d, r, r, u, u, l, l, l, d, d, d, r, r, r, r, u, u, u, u
        for j in range(2):
            for _ in range(i // 2):
                nx = x + direction_r[(i + j) % 4 - 2]
                ny = y + direction_c[(i + j) % 4 - 2]
                if arr[x][y] == 0 and not (x == (n - 1) / 2 and y == (n - 1) / 2):
                    pass
                else:
                    lst.append(arr[x][y])
                x, y = nx, ny
    for k in range(len(lst), n*n):
        lst.append(0)
    return lst


# 2. 구슬 폭발
def blast(lst):
    global blast_marble
    length = len(lst)
    while True:
        flag = True
        n_lst = []
        i = 0
        while i < len(lst) - 1:
            item = lst[i]
            if item != lst[i + 1]:
                n_lst.append(item)
                i += 1
            else:
                k = i
                count = 0
                while k < len(lst) and lst[k] == item:
                    count += 1
                    k += 1
                if count < 4:
                    for _ in range(count):
                        n_lst.append(item)
                else:
                    for _ in range(count):
                        blast_marble.append(item)
                    flag = False
                i = k

        if flag:
            break
        lst = n_lst[:]

    j = len(n_lst)
    while j < length:
        n_lst.append(0)
        j += 1
    lst = n_lst[:]
    return lst


# 3. 구슬 확장
def expand_skill(lst):
    n_lst = [0]
    i = 1
    while i < len(lst):
        item = lst[i]
        if lst[i] == 0:
            break
        if item != lst[i + 1]:
            n_lst.append(1)
            n_lst.append(item)
            i += 1
        else:
            k = i
            count = 0
            while k < len(lst) and lst[k] == item:
                count += 1
                k += 1
            n_lst.append(count)
            n_lst.append(item)
            i = k

    for _ in range(len(n_lst), n * n):
        n_lst.append(0)
    return n_lst


# 4. count 1*(1번 구슬) + 2*(2번 구슬) + 3*(3번 구슬)
def count(lst):
    c = Counter(lst)
    result = 0
    for k, v in c.items():
        result += k * v
    return result


def solution():
    # 0. 구슬 담기
    global n, m, array, attack, blast_marble
    if n < 3 or n > 49:
        return
    if n % 2 != 1:
        return
    if m < 0 or m > 101:
        return

    for d, s in attack:
        if d < 0 or d > 5:
            return
        if s < 0 or s > int((n - 1) / 2) + 1:
            return
        blizard(array, d, s)
        lst = move(array, int((n - 1) / 2), int((n - 1) / 2))
        array_reset(lst, array)
        n_lst = blast(lst)
        array_reset(n_lst, array)
        nn_lst = expand_skill(n_lst)
        array_reset(nn_lst, array)
        result = count(blast_marble)

    print(result)


solution()