# 쿼드 트리
import sys

N = int(sys.stdin.readline())
pos = []
for _ in range(N):
    pos.append(list(map(int, sys.stdin.readline().strip())))


# 분할정복
def divide(x, y, size):
    type = pos[y][x]
    flag = False #

    for i in range(x, x+size):
        if flag == True:
            break
        for j in range(y, y+size):
            # type과 다른 숫자가 있을 때
            if pos[j][i] != type:
                print('(', end='')
                divide(x, y, size//2)
                divide(x+size//2, y, size//2)
                divide(x, y+size//2, size//2)
                divide(x+size//2, y+size//2, size//2)

                print(')', end='')
                flag = True
                break

    # 사이즈 안에서 type과 다른 숫자가 없었을 때
    if flag == False:
        if type == 1:
            print(1, end='')
        elif type == 0:
            print(0, end='')

# main함수
divide(0, 0, N)
