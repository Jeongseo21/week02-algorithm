num, needs = tuple(map(int, input().split()))
trees = list(map(int, input().split()))

# 중간 인덱스의 숫자로 돌려보고 구해진 나무의 크기가 니즈보다 많으면 숫자를 더 키우고 니즈보다 적으면 숫자를 줄임

# h를 넣었을 때 얻는 나무의 길이를 리턴해주는 함수
def get_len(h):
    global trees
    get_len = 0
    for tree in trees:
        if tree - h > 0:
            get_len += (tree - h)
    return get_len

# answer = []
def recurs(needs, start, end):
    global trees
    if end-start == 1:
        print(start)
        return
    mid = (start + end) // 2
    len = get_len(mid)
    if len == needs:
        print(mid)
        return
    elif len < needs:
        recurs(needs, start, mid)
    else:
        recurs(needs, mid, end)


max_h = (0+max(trees))
recurs(needs, 0, max_h)