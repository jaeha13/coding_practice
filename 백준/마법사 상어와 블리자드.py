from collections import Counter

# 0. 구슬 담기
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

attack = []
for j in range(m):
    attack.append(list(map(int, input().split())))

# 0.1 board_printer()
def board_printer(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='\t')
        print()


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
    board_printer(arr)


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
                    arr[x][y] = arr[nx][ny]
                    arr[nx][ny] = 0
                lst.append(arr[x][y])
                x, y = nx, ny
    board_printer(arr)

# 2. 구슬 폭발
# def blast(arr):

# 3. 구슬 확장


# 4. count 1*(1번 구슬) + 2*(2번 구슬) + 3*(3번 구슬)
for d, s in attack:
    print(d, s)
    blizard(array, d, s)
    print()
    for _ in range(s):
        move(array, int((n - 1) / 2), int((n - 1) / 2))
        print()