def quick_sort(array):
    # 리스트의 원소가 1개 이하면 이미 정렬된 것이므로 그대로 반환
    if len(array) <= 1:
        return array

    pivot = array[0]      # 첫 번째 원소를 피벗으로 지정
    tail = array[1:]      # 피벗을 제외한 나머지 원소들

    # 피벗보다 작은 수들만 골라서 왼쪽 리스트 구성
    left_side = [x for x in tail if x <= pivot]
    # 피벗보다 큰 수들만 골라서 오른쪽 리스트 구성
    right_side = [x for x in tail if x > pivot]

    # 분할된 왼쪽 그룹과 오른쪽 그룹을 각각 다시 정렬한 뒤 피벗과 합침
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(array))