# 랜선 자르기

K, N = tuple(map(int, input().split()))

lans = []
for _ in range(K):
    lans.append(int(input()))

start = 1
end = max(lans) # 아주 짧은 랜선은 사용하지 않아도 되니까
ans = 0
while start <= end:
    mid = (start + end)//2
    cnt = 0
    for lan in lans:
        cnt += lan//mid
    if cnt >= N:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1
print(ans)


