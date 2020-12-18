

import sys
# main함수
array = []
ptr = 0
n = int(input())
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        array.append(int(order[1]))
        ptr += 1
    elif order[0] == 'pop':
        if ptr == 0:
            print(-1)

        else:
            print(array.pop(-1))
            ptr -= 1
    elif order[0] == 'size':
        print(ptr)
    elif order[0] == 'empty':
        if ptr == 0:
            print(1)
        else:
            print(0)
    else:
        if ptr == 0:
            print(-1)
        else:
            print(array[-1])
