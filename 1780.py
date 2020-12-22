# 종이의 개수

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
print(board)
cnt_1 = 0
cnt_0 = 0
cnt_r1 = 0
def divide(x, y, size):
    global board
    global cnt_1, cnt_0, cnt_r1
    temp_1 = 0
    temp_0 = 0
    temp_r1 = 0
    for i in range(x, size):
        for j in range(y, size):
            if board[i][j] == 1:
                temp_1 += 1
            elif board[i][j] == 0:
                temp_0 += 1
            else:
                temp_r1 += 1
    if temp_1 == size**2:
        cnt_1 += 1

    elif temp_0 == size**2:
        cnt_0 += 1

    elif temp_r1 == size**2:
        cnt_r1 += 1

    else:
        divide(x, y, size//3)
        divide(x+size//3, y, size//3)
        divide(x+2*(size//3), y, size//3)
        divide(x, y+(size//3), size//3)
        divide(x, y+2*(size//3), size//3)
        divide(x+size//3, y+size//3, size//3)
        divide(x+2*(size//3), y+size//3, size//3)
        divide(x + size // 3, y+2*(size//3), size // 3)
        divide(x+2*(size//3), y + 2 * (size // 3), size // 3)

divide(0, 0, N)
print(cnt_1, cnt_0, cnt_r1)