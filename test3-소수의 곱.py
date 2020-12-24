# 시간초과 나옵니다..

from itertools import combinations_with_replacement
import heapq

# 곱하기 함수
def multiply(arr):
    return eval('*'.join(arr))


K, N = map(int, input().split())
primes = input().split()
result = []
flag = False
# 중복 조합 구하기
for i in range(1, (N+1)//K):
    for i in combinations_with_replacement(primes, i):
        # print(i, end=" ")
        # print(multiply(i))
        heapq.heappush(result, multiply(i))


# 힙큐에서 N번째로 뺀 수 구하기
for i in range(N):
    if i == N-1:
        print(heapq.heappop(result))
    else: heapq.heappop(result)
