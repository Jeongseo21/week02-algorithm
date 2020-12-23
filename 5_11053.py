# 가장 긴 증가하는 수열

N = int(input())
array = list(map(int, input().split()))
dp = [0]*N
max_num = 0

for i in range(len(array)):
    for j in range(i):
        if array[j] < array[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
    max_num = max(dp[i], max_num)

print(max_num)