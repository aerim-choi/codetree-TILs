import sys
sys.setrecursionlimit(2500)

#안전 영역의 수 최대 K와 그 때의 안전 영역 수 구하기
def dfs(x,y,k,matrix):
    
    visited[x][y]=1
    #좌우하상
    d = [(0,1),(0,-1),(-1,0),(1,0)]
    for dx,dy in d:
        newX, newY = x+dx , y+dy
        if check_range(newX,newY) and matrix[newX][newY]>k:
            dfs(newX,newY,k,matrix)
    


def check_range(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    if visited[x][y]==1:
        return False
    else:
        return True



N, M = tuple(map(int,input().split()))

matrix= []
for i in range(N):
    matrix.append(list(map(int,input().split())))

max_range_K = 1
max_result = 0
max_k=1
for i in range(N):
    max_range_K = max(max_range_K, max(matrix[i]))

for k in range(1,max_range_K+1):
    copy_matrix =[[0 for _ in range(M)]for _ in range(N)]
    visited =[[0 for _ in range(M)]for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            copy_matrix[i][j]= matrix[i][j]

    for i in range(N):
        for j in range(M):
            if copy_matrix[i][j]>k and check_range(i,j):
                result+=1
                dfs(i,j,k,copy_matrix)
    
    if max_result<result:
        max_k =k
        max_result=result

print(max_k,max_result)