"""
당신은 음식점의 계산을 도와주는 점원이다. 카운터에서는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리 동전이 무한하다고 존재.
손님에게 거슬러 줘야할 돈이 N원일때, 거슬러줘야 할 동전의 최소 개수는? 단, 거슬러줘야할 돈 N은 항상 10의 배수.

"""
# / 실수 나눗셈
# // 정수 나눗셈

coins = [500, 100, 50, 10]
guest_money = 2900 # 지불한 금액
save = 0 # 남은 돈
N = 0 # 거슬러줘야 할 동전 개수
for i in coins:
    N += guest_money // i
    save = guest_money % i
    guest_money = save
  
print(N)

"""
개선된 코드
"""

n = 1260
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

# N을 구하는 가장 기본적인 방법은 금액 // coin을 나누는것
# 남은 금액은 당연히 업데이트 돼야하고
# 남은 금액은 반드시 % 지로 계속해서 나눠야 한다!
