def check_xy(x,y):
    return x >=0 and x<n and y>=0 and y<m
        
def can_go(x,y):
    if not check_xy(x,y):
        return False
    if visited[x][y] or matrix[x][y]==0:
        return False
    return True



def dfs(x,y):
    dxs = [1,0]
    dys = [0,1]
    
    for dx,dy in zip(dxs,dys):   
        new_x, new_y = x+dx, y+dy
        if can_go(new_x,new_y):
            visited[new_x][new_y]=1
            dfs(new_x,new_y)


n, m = map(int, input().split())

visited = []
for i in range(n):
    visited.append([])
    for j in range(m):
        visited[i].append(0)

matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

dfs(0,0) #시작점에는 뱀이 주어지지 않음

if visited[n-1][m-1]==1:
    print(1)
else:
    print(0)