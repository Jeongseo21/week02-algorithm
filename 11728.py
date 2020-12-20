from sys import stdin

N, M = tuple(map(int, stdin.readline().split()))

A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A.extend(B)
A.sort()
print(' '.join(map(str, A)))
