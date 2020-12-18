# 색종이 자르기

N = int(input())
pos = []
b_cnt, w_cnt = 0, 0
for _ in range(N):
    pos.append(list(map(int, input().split())))

def divide(x, y, N):
    global b_cnt
    global w_cnt
    temp_cnt = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if pos[i][j] == 1:
                temp_cnt += 1
    if temp_cnt == N*N:
        b_cnt += 1
    elif temp_cnt == 0:
        w_cnt += 1
    else:
        divide(x, y, N//2)
        divide(x+N//2, y, N//2)
        divide(x, y+N//2, N//2)
        divide(x+N//2, y+N//2, N//2)
    return

divide(0, 0, N)
print(w_cnt)
print(b_cnt)