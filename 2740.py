# 행렬의 곱셈

import numpy as np

N, M = map(int, input().split())
A = []
# N*M 행렬 완성
for _ in range(N):
    A.append(list(map(int, input().split())))

# M*K 행렬 완성
M, K = map(int, input().split())
B = []
for _ in range(M):
    B.append(list(map(int, input().split())))

# 행렬 곱셈
C = [[0]*K for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            C[n][k] += A[n][m] * B[m][k]
C = np.array(C)
print(C)