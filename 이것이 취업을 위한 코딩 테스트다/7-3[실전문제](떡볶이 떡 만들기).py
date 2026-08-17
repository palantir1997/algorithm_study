"""
문제

동빈이네 떡집에 손님이 떡을 사러 왔을 때, 절단할 수 있는 가장 긴 높이를 출력해라.

동빈이네 떡집에 19 15 10 17 짜리 떡이 있고 절단기가 15일 경우, 손님은 4+0+0+2=6 길이의 떡을 가져가게 된다.

문제 조건

첫 번째 줄에 동빈이네 떡집 떡 개수 N과 손님이 가져가고 싶어하는 양 M이 입력된다.
두 번째 줄에 동빈이네 떡집 떡들의 각자 길이가 N개에 걸쳐 공백으로 구분되어 입력된다.
동빈이가 선택할 수 있는 가장 긴 길이의 절단기 길이를 구해라.
 
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    # mid대신 손님이 원하는 양인 m과 비교해야 한다!.
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)