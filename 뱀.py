# 뱀
import sys
import numpy as np
from collections import deque

dq = deque()
# 실행
board_N = int(sys.stdin.readline())
board = [[0 for _ in range(board_N)] for _ in range(board_N)]

apple_N = int(sys.stdin.readline())

for _ in range(apple_N):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

board = np.array(board)

turn_N = int(sys.stdin.readline())
turn_list = [list(map(str, sys.stdin.readline().split())) for _ in range(turn_N)]
time = 0
# 우 = 1 하 = 2 좌 = 3 상 = 0  방향
direction = 1
x,y = 0,0
dq.append((x,y))
def move():
    global time
    global direction
    global x, y
    time += 1


    if direction == 1:
        x += 1
    if direction == 2:
        y += 1
    if direction == 3:
        x -= 1
    if direction == 0:
        y -= 1
    if time == int(turn_list[0][0]):
        direction = turn_snake(direction, turn_list[0][1])
        turn_list.remove(turn_list[0])

    return

def turn_snake(dir, which):
    if which == 'D':
        dir = (dir + 1) % 4
    else: dir = (dir + 3) % 4
    return dir


while True:
    move()
    print((x,y))
    if (x,y) in dq or x<0 or y<0 or x>=board_N or y>=board_N:
        break
    if board[y][x] == 1:
        dq.append((x,y))
    else:
        dq.append((x,y))
        dq.popleft()
    print(dq)



print(time)