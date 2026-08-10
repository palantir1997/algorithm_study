"""
예제 4-2) 시각
- hh:mm:ss 형태의 시각의 경우의 수를 센다.
- N이 입력되면 00:00:00 부터 N:59:59 까지의 N이 포함된 시각의 개수를 센다.
- 0 <= N <= 23
- 10 이상의 수가 N으로 입력되면, hh, mm, ss 가 10 일 때의 경우의 수만 센다.

<문제풀이>
3중 포문으로 풀으라고 나옴

브루트포스 문제
"""

N = int(input())
count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)
