
brackets = input()
stack = []
count = 0

for i in range(len(brackets)):
    if brackets[i] == "(":
        stack.append('(')
    else:
        # 이전 괄호가 닫는 괄호이면 레이저
        if brackets[i-1] == '(':
            count += len(stack)-1
            stack.pop()
            # 아니면 막대기
        else:
            count += 1
            stack.pop()
print(count)