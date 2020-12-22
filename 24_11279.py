import heapq
import sys

N = int(sys.stdin.readline())
orders = []
heap = []

for i in range(N):
    order = int(sys.stdin.readline())

    if order == 0:
        # 만약 heap이 비어있으면
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-order, order))


