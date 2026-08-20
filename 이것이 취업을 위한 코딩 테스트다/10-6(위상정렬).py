# 먼저 해야 하는 걸 큐에서 빼고 -> 그 뒤에 연결된 애들의 진입차수를 깎고 -> 0이 되면 큐에 넣는
from collections import deque

# 1. 노드의 개수(v)와 간선의 개수(e) 입력받기
v, e = map(int, input().split())

# 2. 모든 노드에 대한 진입차수(In-degree)를 0으로 초기화
# * 진입차수란? "나로 들어오는 화살표의 개수" (즉, 나보다 먼저 끝내야 하는 선행 작업의 개수)
indegree = [0] * (v + 1)

# 3. 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 4. 방향 그래프의 모든 간선 정보 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능 (A를 먼저 해야 B를 할 수 있음)
    
    # B로 들어오는 화살표가 생겼으므로, B의 진입차수를 1 증가시킵니다.
    indegree[b] += 1

# 5. 위상 정렬 함수 정의
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐(Queue) 기능을 위한 deque 라이브러리 사용
    
    # 5-1. 처음 시작할 때는 진입차수가 0인(즉, 선행 작업이 없는) 노드를 큐에 모두 넣습니다.
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
            
    # 5-2. 큐가 빌 때까지 반복
    while q:
        # 큐에서 노드 하나를 꺼냅니다.
        now = q.popleft()
        result.append(now) # 결과 리스트에 담아줍니다 (이 작업이 완료된 순서)
        
        # 해당 노드와 연결된 노드들의 진입차수를 1씩 빼줍니다.
        for i in graph[now]:
            indegree[i] -= 1
            
            # 만약 빼줬는데 진입차수가 0이 되었다면? (모든 선행 작업이 끝났다면!)
            if indegree[i] == 0:
                q.append(i) # 큐에 새로 넣어 다음 작업으로 준비시킵니다.
                
    # 5-3. 결과 출력
    print("위상 정렬 결과: ", end='')
    for i in result:
        print(i, end=' ')

# 위상 정렬 함수 실행
topology_sort()