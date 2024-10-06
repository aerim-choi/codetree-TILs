def check_go(x,y):
    if 0>x or x>=n or 0>y or y>=n:
        return False 
    if visited[x][y]==1 or matrix[x][y]==0:
        return False

    visited[x][y]=1
    return True


def dfs(x,y,depth):
    ds = [(1,0),(-1,0),(0,1),(0,-1)]
    for (dx,dy) in (ds): #상하좌우
        newX = x+dx
        newY = y+dy 
    
        #벽이 없어서 갈 수 있는지 확인 
        if check_go(newX,newY):
            depth+=1
            depth = dfs(newX,newY,depth)
            
    return depth


n = int(input())
result = []
visited = [[0 for _ in range(n)]for _ in range(n)]

matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        global people_count
        if check_go(i,j):
            people_count = dfs(i,j,1)
            if people_count>0:
                result.append(people_count)


print(len(result))
result.sort()

for i in result:
    print(i)