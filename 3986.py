# stack[-1]이랑 비교해서 같으면 pop(), 다르면 append()

N = int(input())
array = []
for _ in range(N):
    array.append(input())
stack = []
cnt = 0
for string in array:
    stack = []
    for i in range(len(string)):
        if not stack:
            stack.append(string[i])
        else:
            if string[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(string[i])

    if stack == []:
        cnt += 1
print(cnt)