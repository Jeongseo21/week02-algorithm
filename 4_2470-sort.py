def search(array, left, right):
    temp = array[left] + array[right]
    if temp == 0:
        print(array[left], array[right])
    if temp < 0:
        search(array, left+1, right)
    elif temp > 0:
        search(array, left, right-1)


N = int(input())
array = list(map(int, input().split()))
array.sort()

# 음수만 있는 경우
if array[-1] <= 0:
    result = [array[-1], array[-2]]
    # print(f'{array[-1]} {array[-2]}')

# 양수만 있는 경우
elif array[0] >= 0:
    result = [array[0], array[1]]
else:
    search(array, 0, len(array)-1)
# print(answer)

'''
abs_num = 2e9
for i in range(len(answer)):
    temp = abs(answer[i][0] + answer[i][1])
    if abs(temp) < abs_num:
        abs_num = temp
        result = [answer[i][0], answer[i][1]]
print(result)
'''