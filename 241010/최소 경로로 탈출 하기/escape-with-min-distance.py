from collections import deque

n,m = map(int, input().split())
#최소 경로로 탈출하기-> bfs
#bfs를 위한 visited
visited = [[0 for _ in range(m)]for _ in range(n)]
#bfs로 탐색하기 위해 queue생성
q=deque()
#시작점으로부터의 최단거리를 저장해줄 step이라는 이름의 이차원 배열
step = [[0 for _ in range(m)]for _ in range(n)]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m
def can_go(x,y):
    if not in_range(x,y): #그래프를 벗어났다면
        return False
    if visited[x][y] == 1 : #방문했다면
        return False
    if graph[x][y]==0: #뱀이 있다면
        return False
    return True

def push(x,y,s):
    step[x][y]=s
    visited[x][y]=1
    q.append((x,y))

#bfs
def bfs():

    #상하좌우
    dxs = [0,0,-1,1]
    dys = [1,-1,0,0]
    while q:
        curr_x, curr_y = q.popleft()
        for dx, dy in zip(dxs,dys):
            new_x ,new_y = curr_x+dx , curr_y+dy
            if can_go(new_x,new_y):
                push(new_x,new_y, step[curr_x][curr_y]+1)

# 뱀 그래프 입력
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

push(0,0,0)
bfs()

print(step[n-1][m-1])