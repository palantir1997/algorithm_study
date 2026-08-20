# 1. 특정 원소가 속한 집합의 대장(루트)을 찾는 함수 (경로 압축 적용)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 2. 두 원소가 속한 집합을 합치는 함수 (Union)
def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

# 노드의 개수(v)와 간선(e) 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 부모 테이블상에서, 처음에는 각자 자기가 자기 자신을 대장으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 사이클 발생 여부 플래그
cycle = False

# 3. 간선을 하나씩 확인하면서 사이클 판별하기
for i in range(e):
    a, b = map(int, input().split())
    
    # ★ [핵심 포인트] 두 노드의 대장이 이미 같다면?
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True  # 이미 같은 집에 속해 있는데 또 연결하려 하므로 사이클 발생!
        break         # 더 볼 것도 없이 반복문 탈출
    else:
        # 대장이 다르다면, 두 집합을 하나로 합쳐줌(Union)
        union_parent(parent, a, b)

# 4. 결과 출력
if cycle:
    print("사이클이 발생했습니다! (무한 루프 구조 존재)")
else:
    print("사이클이 발생하지 않았습니다. (안전한 트리 구조)")