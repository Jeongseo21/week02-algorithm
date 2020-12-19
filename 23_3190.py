N = int(input())

pos = [[0]*N for i in range(N)] # N * N 이차원배열 선언

apple_num = int(input())

# 사과있는 부분 표시
for i in range(apple_num):
    ay, ax = map(int, input().split())
    pos[ay-1][ax-1] = -1

# 현재 위치, 방향 초기화
head_x, head_y = 0, 0
long = 1
dir = 0
cnt = 0
dx = [1, 0, -1, 0]
dy = [0, +1, 0, -1]
endpoint = 0

order_num = int(input())

while True:
    print(pos)
    order = tuple(input().split())
    for i in range(int(order[0])):
        nx = head_x + dx[dir]
        ny = head_y + dy[dir]

        if nx<0 or nx>N or ny <0 or ny>N:
            print(cnt-1)
            endpoint = 1
            break
        elif pos[ny][nx] == -1:
            long += 1
        else:
            cnt += 1
            head_x, head_y = nx, ny
            pos[head_y][head_x] = cnt
    if endpoint == 1:
        break

    if order[1] == 'D':
        dir = (dir + 1) % 4
    else:
        dir = (dir + 3) % 4

print(cnt)



