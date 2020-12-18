# 쇠막대기

case = input()
stack = []
count = 0

for i in range(len(case)):
    if case[i] == "(":
        stack.append('(')
    else:
        if case[i-1] == '(':
            count += len(stack)-1
            stack.pop()
        else:
            count += 1
            stack.pop()
print(count)
