# 뱀

from collections import deque


N = int(input())    # 보드의 크기 N

K = int(input())    # 사과의 개수 K

time = 1       # 현재 시각

dq = deque()    # 뱀이 밟고 있는 좌표를 큐에 저장

pos = [[0]*N for _ in range(N)] # 전체 맵을 pos에 저장

for _ in range(K):     # 사과가 있는 위치
    ax, ay = tuple(map(int, input().split()))
    pos[ax-1][ay-1] = 1

def turn(dir, x, y):
    if dir == 1:    # 우
        x += 1
    elif dir == 2:  # 하
        y += 1
    elif dir == 3:  # 좌
        x -= 1
    else:           # 상
        y -= 1
    return x, y

def move(endtime, dir, x, y):
    global time

    while time <= endtime:
        time += 1  # 시간이 1초 증가

        nx, ny = turn(dir, x, y)# 이동해야할 발판 찾음
        print(nx,ny)
        if nx < 0 or nx > N-1 or ny < 0 or ny> N-1 or (nx, ny) in dq:     # 좌표 밖으로 나갔을 때 혹은 몸통에 부딪혔을 때
            return time
        x, y = nx, ny
        dq.append((x, y))
        if dq == []:
            dq.append(pos[x][y])
        elif pos[x][y] == 1:
            dq.append(pos[x][y])
            pos[x][y] = 0
        else:
            dq.append(pos[x][y])
            dq.popleft()

order_cnt = int(input())

for i in range(order_cnt):
    if i == 0:
        x, y = move(endtime, dir, 0, 0)
    else:
    endtime, dir = input().split()
    x, y = move(endtime, dir, 0, 0)
    if dir == 'D':
        dir = (dir + 1) % 4
    else:
        dir = (dir + 3) % 4

print(x, y)






