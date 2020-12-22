from collections import deque

N = int(input())

pos = [[0]*N for i in range(N)] # N * N 이차원배열 선언

apple_num = int(input())

# 사과있는 부분 표시
for i in range(apple_num):
    ay, ax = map(int, input().split())
    pos[ay-1][ax-1] = -1

# 현재 위치, 방향 초기화
head_x, head_y = 0, 0
dq = deque # 뱀의 몸이 걸쳐있는 pos 저장
dir = 0
time = 0
long = 1
dx = [1, 0, -1, 0]
dy = [0, +1, 0, -1]
endpoint = 0

order_num = int(input())

def turn(order):
    global dir
    # 우:1, 하:2, 좌:3, 상:4
    if order == 'D':
        dir = (dir + 1) % 4
    else:
        dir = (dir + 3) % 4
    return dir

while True:
    order_num -= 1
    if order_num >= 0:
        order = tuple(input().split())
    move = 0

    while int(order[0]) > move:
        move += 1
        nx = head_x + dx[dir]
        ny = head_y + dy[dir]

        if nx<0 or nx>=N or ny <0 or ny>=N:
            print(time)
            endpoint = 1
            break
        elif pos[ny][nx] == -1:
            long += 1
            time += 1
            head_x, head_y = nx, ny
            pos[head_y][head_x] = time
        else:
            time += 1
            head_x, head_y = nx, ny
            pos[head_y][head_x] = time
        print(pos)
        print("long :", long)
        print("cnt :", time)
    dir = turn(order[1])

    if endpoint == 1:
        break


print(time+1)



