"""
💻 컴퓨터 세계에서의 이진 탐색 조건
컴퓨터가 이 기적의 탐색을 하려면 딱 한 가지 절대적인 조건이 필요합니다.
	•	데이터가 반드시 정렬되어 있어야 합니다. (오름차순이든 내림차순이든 순서대로 줄을 서 있어야 함)
	•	정렬도 안 되어 있는데 반으로 쪼개면 큰일 납니다. 엉뚱한 동네를 잘라버리게 되니까요!
⚙️ 코드로 보는 핵심 원리 (변수 3총사)
이진 탐색 코드를 짜거나 이해할 때는 딱 세 가지 위치만 기억하면 됩니다.
	1	start: 탐색할 범위의 맨 왼쪽(시작점) 인덱스
	2	end: 탐색할 범위의 맨 오른쪽(끝점) 인덱스
	3	mid: start와 end의 정가운데 인덱스 ((start + end) // 2)
이 mid 지점의 값과 내가 찾는 목표 값을 비교해서:
	•	목표가 더 크다? $\rightarrow$ 왼쪽 절반은 버리고 start를 mid + 1로 옮깁니다.
	•	목표가 더 작다? $\rightarrow$ 오른쪽 절반은 버리고 end를 mid - 1로 옮깁니다.

"""

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재 X")
else:
    print(result + 1)