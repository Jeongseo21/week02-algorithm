
N = int(input())
cards = list(map(int, input().split())) # 내가 가지고 있는 카드
cards.sort()
M = int(input())
nums = list(map(int, input().split())) # 기준이 되는 수


# 이진탐색으로 같은 수 찾으면 앞, 뒤 확인

def recurs(cards, start, end, target, cnt):
    mid = (start + end)//2
    if start > end:
        return 0
    if cards[mid] == target:
        return cards[start:end+1].count(target)
    elif cards[mid] < target:
        return recurs(cards, mid+1, end, target, cnt)
    else:
        return recurs(cards, start, mid-1, target, cnt)


for num in nums:
    print(recurs(cards, 0, N, num, 0), end=' ')