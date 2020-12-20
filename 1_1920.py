n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

# 시간복잡도 O(N^2) -> 100000 * 100000 = 10000000000
for i in x:
    if i in array:
        print('1')
    else:
        print('0')

