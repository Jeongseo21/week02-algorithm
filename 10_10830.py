# 행렬의 제곱

# 행렬 곱셈

def mul(n, matrix1, matrix2):
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000
    return result #곱해진 행렬을 리턴


# 2분할
def divide(n, b, matrix):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(n, matrix,matrix)
    else:
        temp = divide(n, b//2, matrix)
        # 제곱수가 2의 배수일 때
        if b % 2 == 0:
            return mul(n, temp, temp)
        # 제곱수가 홀수일 때
        else:
            return mul(n,mul(n, temp, temp), matrix)


# 입력
n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

result = divide(n, b, a)

for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()


###########################################
'''
N, B = map(int, input().split())

mat = []

for i in range(N):
    mat.append(list(map(int, input().split())))


def mat_product(matrix1, matrix2):
    l = len(matrix1)
    l_1 = len(matrix1[0])
    l_2 = len(matrix2[0])

    m = []

    for i in range(l):
        m_ = []

        for j in range(l_2):
            s = 0
            for k in range(l_1):
                s += matrix1[i][k] * matrix2[k][j]
            s = s % 1000
            m_.append(s)
        m.append(m_)
    return m


a = mat.copy()
b = 0
while True:
    if B == 0:
        break

    if B % 2 == 1:
        if b == 0:
            b = a
        else:
            b = mat_product(a, b)

    B //= 2
    a = mat_product(a, a)

#출력
for i in range(N):
    for j in range(N):
        print(b[i][j] % 1000, end=' ')
    print()
'''
