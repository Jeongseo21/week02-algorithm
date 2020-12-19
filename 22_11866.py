'''
from collections import deque
import time
start = time.time()
dq = deque()
N, K = map(int, input().split())

array = []
for i in range(1, N+1):
    array.append(i)

answer = []
flag = [0]*N
cnt = 0

while 0 in flag:
    for num in array:
        if flag[num-1] == 0:
            dq.append(num)
            cnt += 1
            if cnt % K == 0 and cnt != 0:
                target = dq.pop()
                answer.append(str(target))
                flag[target-1] = 1
print(f"<{', '.join(answer)}>")

print(time.time()-start)
'''
###########################################
#보석오빠 풀이
from collections import deque
import sys
# 인스턴스 생성
q = deque()
# 명령 실행
N, K = map(int, sys.stdin.readline().split())

for i in range(1,N+1):
    q.append(i)

print('<',end='')
while len(q)>1:
    for _ in range(K-1):
        q.append(q.popleft())
    x = q.popleft()
    print(f'{x}, ',end='')

x = q.popleft()
print(f'{x}>')

