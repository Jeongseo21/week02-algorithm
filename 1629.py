A, B, C = tuple(map(int, input().split()))

array = [0]*(C)

for i in range(1, C):
    array[i] = (A**i) % C

# C-1을 주기로 반복
print(array)
print(array[B % (C-1)])
