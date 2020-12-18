'''
def binaray_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2

    # target을 찾은 경우 인덱스 반환
    if array[mid] == target:
        return mid

    # 중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
    if array[mid] > target:
        return binaray_search(array, target, start, mid-1)
    else:
        return binaray_search(array, target, mid+1, end)
'''

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # 종료조건
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid-1
    # 만일 target을 못찾은 채로 start가 end보다 커지면
    return None

