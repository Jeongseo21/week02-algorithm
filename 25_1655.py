# 가운데를 말해요
import heapq
import sys
N = int(sys.stdin.readline())

nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

min_heap = []
max_heap = []

def check(num):
    if not min_heap and not max_heap:
        heapq.heappush(max_heap, (-num, num))
    elif len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, num)

    if min_heap and max_heap[0][1] > min_heap[0]:
        max_temp = (heapq.heappop(max_heap))[1]
        min_temp = heapq.heappop(min_heap)
        heapq.heappush(min_heap, max_temp)
        heapq.heappush(max_heap, (-min_temp, min_temp))

        # print('max[0][1]', max_heap[0][1])
        # print('min', heapq.heappop(min_heap))
    return max_heap[0][1]


for i in range(len(nums)):
    print(check(nums[i]))