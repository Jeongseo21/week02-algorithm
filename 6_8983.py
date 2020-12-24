# 사냥꾼

import sys
# import numpy as np
# sys.stdin = open("/Users/jewerlykim/Desktop/week1/백준 문제 파일/week02/baekjoon/txt/6.txt", 'r')
M, N, L = map(int, sys.stdin.readline().split())
shooting = sorted(map(int, sys.stdin.readline().split()))
animals = []
for _ in range(N):
    animals.append(list(map(int, sys.stdin.readline().split())))
# animals = np.array(animals)
# print(shooting)
# print(animals)
count = 0
def count_shoot(left:int, right:int):
    global count
    pl = 0
    pr = len(shooting) - 1
    while pl<=pr:
        pc = (pl + pr) // 2
        if left <= shooting[pc] <= right:
            count += 1
            # print(shooting[pc])
            return
        elif shooting[pc] < left:
            pl = pc + 1
        else:
            pr = pc - 1
    return
for animal in animals:
    if L >= animal[1]:
        gap = L - animal[1]
        # print(animal)
        left = animal[0] - gap
        right = animal[0] + gap
        count_shoot(left, right)
print(count)