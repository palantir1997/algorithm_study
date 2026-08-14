# 모든 부품 번호를 담을 수 있는 크기의 리스트를 0으로 초기화 (1,000,000까지이므로 1000001 크기)
# (파이썬에서는 리스트 곱셈으로 선언하는 것이 가장 빠릅니다)
count = [0] * 1000001

# 가게에 있는 부품 번호를 입력받아 해당 인덱스에 1 기록
n = int(input())
array = list(map(int, input().split()))
for i in array:
    count[i] = 1

# M 손님 부품 개수
m = int(input())
x = list(map(int, input().split()))

# 손님이 요청한 번호가 기록되어 있는지 확인
for i in x:
    # 만약 번호가 1,000,000을 넘어가는 예외 상황이 없다면 바로 확인 가능
    if count[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')