def recur(array, start, end, num1):
    global answer
    # 종료 조건
    if start >= end:
        answer.append([num1, array[end]])
        # print("여기는 start > end : "+str(num1)+ " "+str(array[end]))
        return
    mid = (start + end)//2
    if array[mid] + num1 == 0:
        # print(f'여기는 총합이 0 : {num1} {array[mid]}')
        answer.append([num1, array[mid]])

    if array[mid] + num1 < 0:
        recur(array, mid+1, end, num1)
    elif array[mid] + num1 > 0:
        recur(array, start, mid-1, num1)



# main함수
N = int(input())
array = list(map(int, input().split()))
array.sort()
answer = []
result = []

# 음수만 있는 경우
if array[-1] <= 0:
    result = [array[-1], array[-2]]
    # print(f'{array[-1]} {array[-2]}')

# 양수만 있는 경우
elif array[0] >= 0:
    result = [array[0], array[1]]
else:
    for num1 in array:
        array.remove(num1)
        recur(array, 0, N-2, num1)
# print(answer)


abs_num = 2e9
for i in range(len(answer)):
    temp = abs(answer[i][0] + answer[i][1])
    if abs(temp) < abs_num:
        abs_num = temp
        result = [answer[i][0], answer[i][1]]
print(result)

