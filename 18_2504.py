# 괄호의값
import sys
brackets = list(sys.stdin.readline().strip())

stack = []

# 올바 른 괄호인지 판단하기
def valid_brackets(brackets):
    stack = []
    for brack in brackets:
        if brack == '(' or brack == '[':
            stack.append(brack)
        elif brack == ')':
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        else:
            if not stack:
                return False
            if stack[-1] == '[':
                stack.pop()
            else:
                return False
    if not stack:
        return True
    else:
        return False

def num_sum(n):
    rtn = 0
    while True:
        top = stack.pop()
        if top == '(' or top == '[':
            break
        rtn += top

    if rtn:
        return rtn * n
    else:
        return n

# 올바른 괄호라면
if valid_brackets(brackets):
    for brack in brackets:
        if brack == '(' or brack == '[':
            stack.append(brack)
        elif brack == ')':
            stack.append(num_sum(2))
        elif brack == ']':
            stack.append(num_sum(3))
    print(sum(stack))
else:
    print(0)

