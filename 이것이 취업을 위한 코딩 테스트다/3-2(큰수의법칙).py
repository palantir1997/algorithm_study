"""
2019 국가 교육기관 코딩 테스트
첫째줄에 N, M, K 자연수가 주어지고, 각 자연수는 공백으로 구분
둘째 줄에 N 개의 자연수가 주어지고, 각 자연수는 공백으로 구분한다. 각각의 자연수는 1이상 10000 이하 수  
입력으로 주어지는 K는 항상 M 보다 작거나 같다.

예를들어 순서대로 2,4,5,4,6 이루어진 배열이 있다. M이 8, K 3 이라고 가정
이 경우 인덱스의 수가 연속해서 세 번 까지만 더해질 수 있으므로 6+6+6+5+6+6+6+5 = 46

또는 3 4 3 4 3 M=7, K=2일땐,

"""

N, M, K = map(int, input().split()) # 배열 인덱스 개수, 총 더해져야 할 수, 반복하는 수
N = list(map(int, input().split()))
data = sorted(N, reverse=True) # 소팅해서 내림차순으로 만든다.
f_n = data[0]
s_n = data[1]
save = 0
while M > 0:
    for _ in range(K):
        if M == 0:
            break

        save += f_n
        M -= 1

    if M == 0:
        break

    save += s_n
    M -= 1
print(save)

