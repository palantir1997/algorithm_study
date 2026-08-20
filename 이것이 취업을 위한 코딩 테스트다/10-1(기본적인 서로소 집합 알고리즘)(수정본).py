"""
💡 서로소 집합(Union-Find)이 왜 중요할까?
컴퓨터 과학이나 코테에서 "그룹(집합)을 묶고, 같은 그룹인지 빠르게 판별"해야 하는 상황에 무조건 쓰입니다.
친구 관계 판별 (소셜 네트워크): "A와 B가 친구인가?"를 판별할 때 씁니다. (A의 무리와 B의 무리가 서로 연결되어 하나의 거대한 인맥 네트워크가 되었는지 확인)
사이클 판별 (무방향 그래프): 그래프에서 사이클(순환 구조)이 생기는지 확인할 때 필수적입니다. 코테에서 최소 신장 트리(MST)를 구하는 크루스칼(Kruskal) 알고리즘을 쓸 때 이 서로소 집합 코드가 그대로 핵심 부품으로 들어갑니다.
네트워크 연결 상태 관리: 컴퓨터 네트워크나 도로망이 서로 연결되어 통신이 가능한지 확인할 때 유용합니다.

"""
# 특정 원소가 속한 집합의 루트(대장) 노드를 찾는 함수
# ★ [핵심 최적화: 경로 압축] 부모를 찾아 올라가는 길에, 만나는 모든 노드의 부모를 '직속 대장'으로 바꿔버립니다!
def find_parent(parent, x):
    # 만약 자기 자신이 대장이 아니라면 (즉, 부모 테이블에 적힌 값이 자기 자신이 아니면)
    if parent[x] != x:
        # 대장을 찾아 올라가는 재귀 호출 결과를, 내 부모 테이블에 바로 꽂아넣습니다. (경로 압축)
        parent[x] = find_parent(parent, parent[x])
    return parent[x]  # 최종 대장 노드 번호를 반환

# 두 원소가 속한 집합을 하나로 합치는 함수 (Union)
def union_parent(parent, a, b):
    # 각각의 대장(루트 노드)을 찾습니다.
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    
    # 대장이 다르다면 두 집합을 합쳐줍니다.
    if root_a < root_b:
        parent[root_b] = root_a  # 번호가 더 작은 쪽을 대장으로 삼습니다.
    else:
        parent[root_a] = root_b

# 1. 노드의 개수(v)와 간선(union 연산 횟수, e)을 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화 (노드 번호 1번부터 쓰려고 v+1 크기로 생성)

# 2. 부모 테이블상에서, 처음에는 각자 자기가 자기 자신을 대장(부모)으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 3. union 연산을 각각 수행 (간선 정보 입력받아 집합을 합치기)
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 4. 각 원소가 속한 집합(최종 대장)이 누구인지 출력
print("각 원소가 속한 집합(대장): ", end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 5. 부모 테이블 내용 출력 (경로 압축이 완료되어 최종 대장들이 어떻게 꽂혀있는지 확인)
print('부모 테이블 (직속 대장 상태): ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ') 