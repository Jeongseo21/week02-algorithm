
'''
N,K = map(int, input().split())
array = []
nums = input()
for num in nums:
    array.append(int(num))

stack = []
count = 0
def check(array, i):
    global count, K, stack
    if i == 0 or stack == []:
        stack.append(array[i])
    else:
        if stack[-1] < array[i]:
            stack.pop()
            count += 1

            if count == K:
                return stack

            check(array, i)
        elif stack[-1] >= array[i]:
            stack.append(array[i])

    if count >= K:
        return stack


for i in range(len(array)):
        if check(array, i) is not None:
            stack.extend(array[i:])
            stack = map(str, stack)
            print(''.join(stack))
            break

if count != K:
    stack = stack[:-(K-count)]
    stack = map(str, stack)
    print(''.join(stack))
'''

'''
10 5
1924375035

6 2
391123
'''

N, K = map(int, input().split())
string = input()
count = 0
stack = list()
for i in range(len(string)):
    if not stack:
        stack.append(int(string[i]))
    else:
        while True:
            if stack[-1] < int(string[i]) and count < K:
                stack.pop()
                count += 1
                if not stack:
                    stack.append(int(string[i]))
                    break
            else:
                stack.append(int(string[i]))
                break
while count < K:
    stack.pop()
    count += 1
print("".join(map(str, stack)))