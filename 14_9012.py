# 괄호

N = int(input())
cases = []
for _ in range(N):
    cases.append(input())

for case in cases:
    flag = 0
    stack = []
    for char in case:
        if char == '(':
            stack.append(char)
        else:
            if stack != []:
                stack.pop()
            else:
                flag = -1
    if stack == [] and flag == -1:
        print('NO')
    elif stack == []:
        print('YES')
    else:
        print('NO')
