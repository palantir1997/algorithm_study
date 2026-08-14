"""
여기서 우리가 찾는 값이 하필 이 배열에 없는 값이거나, 범위를 좁히다 보니 start와 end가 엇갈리는 상황이 옵니다.
	1	mid = (0 + 1) // 2 이므로 mid = 0이 됩니다.
	2	만약 찾는 값이 array[0]보다 작다면, 우리는 왼쪽 범위를 찾아야 합니다.
	◦	이때 end = mid - 1을 하게 되므로, end = 0 - 1이 되어서 end = -1로 떨어집니다.
	◦	아까 start는 여전히 0이었죠?
	◦	결과: start(0) > end(-1)이 되어버립니다.

"""
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    # start가 end보다 커지면 탐색 범위가 사라진 것이므로 반복문 종료
    while start <= end:
        mid = (start + end) // 2

        # 1. 원소를 찾은 경우
        if array[mid] == target:
            return mid
        
        # 2. 중간점의 값보다 찾고자 하는 값이 작은 경우 (왼쪽 확인)
        elif array[mid] > target:
            end = mid - 1
            
        # 3. 중간점의 값보다 찾고자 하는 값이 큰 경우 (오른쪽 확인)
        else:
            start = mid + 1
            
    # 끝까지 찾지 못한 경우
    return None

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재 X")
else:
    print(result + 1)