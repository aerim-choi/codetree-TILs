from collections import deque

def can_go(x,y):
    if 0>x or n<=x or 0>y or n<=y:#그래프를 벗어남
        return False
    if graph[x][y]==1: #이동할 수 없는 곳은 1
        return False
    if visited[x][y]==1:#방문했던 곳은 1
        return False
    return True

def bfs():
    #상하좌우
    dxs=[0,0,-1,1]
    dys=[1,-1,0,0] 
    while q:
        cx,cy = q.popleft()
        for x,y in zip(dxs,dys):
            new_x,new_y=cx+x, cy+y
            if can_go(new_x,new_y):
                visited[new_x][new_y]=1
                q.append((new_x,new_y))

def count_visited():
    cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1:
                cnt+=1
    return cnt

n, k =tuple(map(int, input().split()))

# 위치 정보를 저장해둘 리스트
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#탐색을 시작할 위치를 저장해둘 리스트
start_vertax = [] 
for _ in range(k):
    start_vertax.append(tuple(map(int, input().split())))

#방문한 곳인지 저장해둘 리스트
visited = [[0 for _ in range(n)]for _ in range(n)]

#bfs를 위해 deque초기화
q = deque()

for x,y in start_vertax:
    visited[x-1][y-1]=1
    q.append((x-1,y-1))
    bfs()


result = count_visited()
print(result)