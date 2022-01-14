#BFS(Breadth First Search) : 너비우선탐색 (가까운 노드부터 탐색하는 알고리즘)
#BFS구현 : 선입선출의 Queue 자료 구조 사용
#1. 탐색시작 노드를 큐에 삽입 + 방문처리
#2. 제일 아래의 노드를 popleft하고 인접 노드 중 방문 안한 노드를 큐에 삽입
#3. 계속 반복 수행

from collections import deque   #큐를 사용하기 위해 필요한 라이브러리

#BFS메서드 정의
def bfs(graph,start,visited):
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재노드를 방문 처리
    visited[start]= True 
    #큐가 빌때까지 반복
    while True:
        #큐에서 하나의 원소를 뽑아 출력(제일 먼저들어간 노드)
        v=queue.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문안한 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True 
                
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 
visited = [False]*9

bfs(graph,1,visited)

