# 1. 특정 원소가 속한 집합의 대장(루트)을 찾는 함수 (경로 압축 적용)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 2. 두 원소가 속한 집합을 하나로 합치는 함수 (Union)
def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

# --- [메인 프로그램 시작] ---

# 3. 노드의 개수(v)와 간선의 개수(e) 입력받기
v, e = map(int, input().split())

# 부모 테이블을 만들고, 처음에는 각자 자기가 자기 자신을 대장으로 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# 4. 모든 간선 정보를 담을 리스트와, 최종 최소 비용을 담을 변수 선언
edges = []
total_cost = 0

# 5. 간선 정보 입력받기 (예: A노드, B노드, 연결 비용)
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용(cost)이 맨 앞에 오도록 튜플로 묶어서 리스트에 넣습니다. (그래야 비용 순으로 정렬하기 편하니까요!)
    edges.append((cost, a, b))

# 6. ★ [크루스칼 핵심 1단계] 간선을 비용이 '가장 싼 것(오름차순)'부터 순서대로 싹 정렬합니다!
edges.sort()

# 7. ★ [크루스칼 핵심 2단계] 가장 싼 간선부터 하나씩 꺼내서 확인하기
for edge in edges:
    cost, a, b = edge
    
    # 두 노드의 대장(루트)이 서로 다르다면? (아직 같은 무리가 아님 = 연결해도 사이클 안 생김)
    if find_parent(parent, a) != find_parent(parent, b):
        # 두 집합을 하나로 합쳐줍니다 (Union)
        union_parent(parent, a, b)
        # 전체 최소 비용에 이 간선 비용을 더해줍니다
        total_cost += cost
        print(f"[선택] 노드 {a}와 노드 {b}를 연결! (비용: {cost})")
    else:
        # 대장이 이미 같다면? 연결하면 둥글게 원형(사이클)이 되므로 과감하게 버립니다!
        print(f"[제외] 노드 {a}와 노드 {b}는 이미 연결되어 있음 (사이클 방지)")

# 8. 모든 노드를 가장 적은 비용으로 연결한 최종 결과(MST 비용) 출력
print(f"\n모든 도시(노드)를 연결하는 최소 비용(MST): {total_cost}")