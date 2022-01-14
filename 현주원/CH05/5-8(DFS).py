#DFS(Depth-First Search) : 깊이 우선탐색

#DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v]=True
    
    print(v,end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph=[[], #0번 노드는 없으므로 비워둠
       [2,3,8], #1번 노드
       [1,7], #2번 노드
       [1,4,5], #3번 노드
       [3,5], #4번 노드
       [3,4], #5번 노드
       [7], #6번 노드
       [2,6,8]  #7번 노드
       [1,7]   #8번 노드
       ]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9    #'9'를 곱해주는 이유: index 0을 사용하지 않기 위해서 1-8(8개)+1된 값 곱 / False: 방문X

#정의된 DFS 함수 호출
dfs(graph,1,visited)    
