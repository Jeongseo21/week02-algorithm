import sys

N = int(sys.stdin.readline().rstrip())
data = []
stack = []
ptr = 0
for _ in range(N):
    data.append(int(sys.stdin.readline().rstrip()))

for i in range(N):
    if i == 0:
        stack.append(data[i])
        ptr += 1
    while data[i] >= stack[-1]:
        # print(f'{stack[-1]} 나갔다')
        stack.pop()
        ptr -= 1
        if i == 1 or not stack:
            break
    stack.append(data[i])
    ptr += 1
    # print(stack)
    # print(f"{data[i]} 들어왔다")
sys.stdout.write(str(ptr))