'''
x = int(input())
cnt = 0

while x != 1:
    if (x-1) % 3 == 0:
        x -= 1
    elif x % 3 == 0:
        x = x // 3
    elif x % 2 == 0:
        x = x // 2
    else:
        x -= 1
    cnt += 1
print(cnt)
'''

x = int(input())
dp = [0]*1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1

for n in range(4, x+1):
    dp[n] = 1 + dp[n-1]
    if n % 3 == 0 and dp[n] > dp[n//3]+1:
        dp[n] = dp[n//3]+1
    if n % 2 == 0 and dp[n] > dp[n//2]+1:
        dp[n] = dp[n//2] +1
print(dp[x])