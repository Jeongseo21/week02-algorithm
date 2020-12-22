N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

minus = 0
plus = 0
zero = 0

def nine_tree(x, y, size):
    global minus, plus, zero, matrix
    type = matrix[y][x] # 첫 타일의 번호 저장
    double_break = False

    for i in range(x, x+size):
        if double_break:
            break
        for j in range(y, y+size):
            if matrix[j][i] != type:

                nine_tree(x, y, size//3)
                nine_tree(x + size//3, y, size//3)
                nine_tree(x + 2 * (size//3), y, size//3)
                nine_tree(x, y + size//3, size//3)
                nine_tree(x + size//3, y + size//3, size//3)
                nine_tree(x + 2 * (size//3), y + size//3, size//3)
                nine_tree(x, y + 2 * (size//3), size//3)
                nine_tree(x + size//3, y + 2 * (size//3), size//3)
                nine_tree(x + 2 * (size//3), y + 2 * (size//3), size//3)

                double_break = True
                break

        if double_break == False:
            if type == 1:
                plus += 1
            elif type == -1:
                minus += 1
            else:
                zero += 1

nine_tree(0,0,N)
print(minus)
print(zero)
print(plus)