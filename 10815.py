# 숫자카드
from sys import stdin

N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
cards.sort()
M = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

for num in nums:
    start = 0
    end = N-1
    while True:
        # 종료조건
        if start > end:
            print(0, end=' ')
            break
        mid = (start + end)//2
        if cards[mid] == num:
            print(1, end=' ')
            break
        elif cards[mid] > num:
            end = mid - 1
        elif cards[mid] < num:
            start = mid + 1


