# 원영역을 뿌셔보자
import sys
# sys.stdin = open("/Users/jewerlykim/Desktop/week1/백준 문제 파일/week02/baekjoon/txt/17.txt", 'r')
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
circle_info = []
count = 1
for _ in range(N):
    center, radius = map(int, sys.stdin.readline().split())
    left_x = center - radius
    right_x = center + radius
    circle_info.append((left_x, 1, -2*radius))
    circle_info.append((right_x, 0, 2*radius))
circle_info.sort(key= lambda x: (x[0], x[1], x[2]), reverse=True)
def cir_count(x, open, R):
    global count
    bigger = 0
    smaller = 0
    while True:
        if open:
            if not bigger:
                bigger = -R
            else:
                smaller += cir_count(x, open, R)
        else:
            if bigger==smaller:
                count += 1
            count += 1
            return bigger
        x, open, R = circle_info.pop()
while len(circle_info):
    x, open, R = circle_info.pop()
    cir_count(x, open, R)
print(count)