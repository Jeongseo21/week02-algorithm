# 카드 정렬
import sys
import heapq

N = int(sys.stdin.readline())
nums = []
total = 0

for i in range(N):
    heapq.heappush(nums, int(sys.stdin.readline()))

for _ in range(N-1):
    x = heapq.heappop(nums)
    y = heapq.heappop(nums)
    z = x + y
    total += z
    heapq.heappush(nums, z)
print(total)


