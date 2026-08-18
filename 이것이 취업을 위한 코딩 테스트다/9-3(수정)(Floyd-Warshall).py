import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한대를 의미하는 값 (도달할 수 없음)

# n: 노드(도시) 개수, m: 간선(도로) 개수
n, m = map(int, input().split())

# 2차원 리스트(그래프 지도)를 만들고, 모든 값을 무한대(INF)로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 가는 비용은 0으로 초기화 (예: 1번 -> 1번은 0원)
for a in range(1, n + 1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력 받아, 초기 비용 테이블 세팅
for _ in range(m):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# ==========================================
# [핵심] 플로이드 워셜 알고리즘 수행 (3중 for문)
# k = 거쳐 가는 노드
# a = 출발 노드
# b = 도착 노드
# ==========================================
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 점화식: K를 거쳐 가는 게 더 빠르면 갱신!
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, "INFINITY"라고 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()   