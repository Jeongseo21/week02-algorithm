# 탑

def check(stack, value):
    if stack == []:
        index.append(str(0))
        stack.append(value)
        return
    elif stack[-1][1] < value[1]:
        stack.pop()
        check(stack, value)
        return
    elif stack[-1][1] > value[1]:
        index.append(str(stack[-1][0]))
        stack.append(value)
        return



N = int(input())
values = list(map(int, input().split()))
array = []

for idx, value in enumerate(values):
    array.append((idx+1, value))

stack = []
index = []
for value in array:
    check(stack, value)

print(" ".join(index))