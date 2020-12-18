# 탑

N = int(input())
stack = list(map(int, input().split()))
answer = []

while stack != []:
    std = stack.pop()
    if stack[-1] > std:
        answer.append(stack[-1])
    else:
        stack.pop()

for _ in range(len(stack)):
    answer.append(0)

print(answer)