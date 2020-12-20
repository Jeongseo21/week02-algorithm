N, C = tuple(map(int, input().split()))

array = []
for _ in range(N):
    array.append(int(input()))
array.sort() # 집의 좌표 오름차순으로 정렬

start = 0 # 공유기 사이 거리 0부터
end = array[-1] - array[0] # 맨 끝집에서 맨 앞집 사이 거리까지
result = 0

while start <= end:
    mid = (start + end)//2
    value = array[0]
    count = 1

    #공유기 설치
    # i번째 집에 공유기를 설치 할 수 있으면 개수 늘리고 value를 i번째 집으로 이동
    for i in range(1, N):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid-1
print(result)


