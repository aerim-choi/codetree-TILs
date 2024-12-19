import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

visited = [False] * (n+1)

dist = [INT_MAX] * (n+1)

for _ in range(m):
    start, end, score = map(int, input().split())

    graph[start][end] = score

#1번 정점부터 다른 모든 정점으로 가는 최단 경로 
#시작위치를 1번
dist[1] = 0 

for i in range(1, n+1):
    min_idx =-1
    for j in range(1, n+1):
        if visited[j]:
            continue
        
        if min_idx == -1 or dist[min_idx] > dist[j]:
            min_idx = j

        #최솟값에 해당하는 정점에 방문 표시를 진행
    visited[min_idx] = True

    #최솟값에 해당하는 정점에 연결된 간선을 보며 
    # 시작점으로부터 최단거리 값을 갱신해줍니다
    for j in range(1, n+1):
        #간선이 존재하지 않는 경우 넘어갑니다 
        if graph[min_idx][j] == 0:
            continue

        dist[j] = min(dist[j], dist[min_idx]+ graph[min_idx][j])

    
for i in range(2,n+1):
    print(dist[i])