from collections import deque
import sys
dq = deque()
front = 0
back = 0
N = int(input())
for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == 'push':
        dq.appendleft(order[1])
        front += 1
    elif order[0] == 'pop':
        if front == 0:
            print(-1)
        else:
            print(dq.pop())
            front -= 1
    elif order[0] == 'size':
        print(front)
    elif order[0] == 'empty':
        if front == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if front == 0:
            print(-1)
        else:
            print(dq[front-1])
    elif order[0] == 'back':
        if front == 0:
            print(-1)
        else:
            print(dq[back])

'''
from collections import deque
dq = deque()

큐를 사용해서 문제 풀 때는 deque 사용하기.
리스트는 원소 하나씩 다 확인해서 평균적으로 O(N)의 시간이 걸리지만
큐는 O(1)의 시간만으로 원소에 접근할 수 있어서 더 빠르다.

인덱스를 설정해서 값을 삽입할 때는 insert
dq.insert(0,1)
dq.insert(0, 2)


dq.popleft()
print(dq)
'''