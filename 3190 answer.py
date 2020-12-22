from sys import stdin
from collections import deque

N = int(stdin.readline())
matrix = [[0]*N for _ in range(N)]

K = int(stdin.readline())
for _ in range(K):
    r, c = map(int, stdin.readline().split())
    matrix[r-1][c-1] = 1

change = {}
I = int(stdin.readline())
for _ in range(I):
    x, c = input().split()
    change[int(x)] = c

snake = deque([(0, 0)])

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 1
time = 0
nx, ny = 0, 0

def turn(direction, d):
    if direction == "D":
        d = (d+1) % 4
    else:
        d = (d+3) % 4
    return d

while True:
    time += 1
    nx += dx[d]
    ny += dy[d]

    if time in change.keys():
        d = turn(change[time], d)

    if nx<0 or nx >=N or ny < 0 or ny >= N or [nx, ny] in snake:
        break
    else:
        if matrix[nx][ny] == 1:
            matrix[nx][ny] = 0
            snake.append([nx,ny])
        elif matrix[nx][ny] == 0:
            snake.append([nx, ny])
            x, y = snake.popleft()
    
print(time)