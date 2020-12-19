from collections import deque

dq = deque()

N = int(input())

for i in range(1, N+1):
    dq.appendleft(i)

while len(dq) > 1:
    dq.pop()
    if len(dq) > 1:
        dq.appendleft(dq.pop())
    else:
        break
print(dq[0])