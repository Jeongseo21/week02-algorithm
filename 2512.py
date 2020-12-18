N = int(input())
needs = list(map(int, input().split()))
limit = int(input())

# 최대 예산을 넣으면 필요한 예산 총액 리턴
def check(height):
    global needs
    total = 0
    for local in needs:
        if local > height:
            total += height
        else:
            total += local
    return total


def recur(start, end):
    if end-start == 1:
        print(start)
        return
    global limit
    mid = (start + end)//2
    total = check(mid)
    if limit > total:
        recur(mid, end)
    elif limit == total:
        print(mid)
        return
    else:
        recur(start, mid)

# 일단 (0, 최대요청예산)으로 시작
max_needs = max(needs)
if max_needs == 0:
    print(0)
elif sum(needs) <= limit:
    print(max_needs)
else:
    recur(0, max_needs)