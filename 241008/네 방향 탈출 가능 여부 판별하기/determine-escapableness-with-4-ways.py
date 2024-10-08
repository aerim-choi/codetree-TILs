from collections import deque
#탈출을 할 수 있는지 없는지니까 상하좌우 탐색 순서는 상관없다.

def bfs():
    #상,하,좌,우
    dxs = [0,0,-1,1]
    dys = [1,-1,0,0]
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            new_x, new_y = x+dx, y+dy

            if can_go(new_x,new_y):
                visited[new_x][new_y]=1
                q.append((new_x,new_y))

    
def can_go(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if visited[x][y]==1 or graph[x][y]==0: #방문했던 곳이나 뱀이 있으면 안됨
        return False
    return True


def check_finish():
    return visited[n-1][m-1]
        

n,m = tuple(map(int, input().split()))

graph = []

# 그래프 만들기
for i in range(n):
    graph.append(list(map(int, input().split())))


# 방문 그래프 만들기
visited = [[0 for _ in range(m)] for _ in range(n)]

# bfs탐색을 위한 queue 초기화
q = deque()

#출발지점
visited[0][0]=1 
q.append((0,0))

bfs() #탐색 시작

#정답 확인
if check_finish():
    print(1)
else:
    print(0)