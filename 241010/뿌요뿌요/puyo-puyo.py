import sys
sys.setrecursionlimit(10**4)

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

#방문정보를 담을 2차원 배열
visited = [[0 for _ in range(n)]for _ in range(n)]

# 터지게 되는 블럭의 수와 최대 블럭의 크기
bump_block = 0
max_block = 0
curr_block_num = 0 

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def can_go(x,y,color):
    if in_range(x,y):
        return False
    if  visited[x][y]==1 :
        return False
    if graph[x][y]!=color:
        return False
    return True

def dfs(curr_x,curr_y):
    global curr_block_num
    
    for x,y in [(0,1),(0,-1),(-1,0),(1,0)]:
        new_x, new_y = curr_x+x , curr_y+y
    
        # 매트릭스를 벗어나지 않았는지, 방문하지 않았는지, 같은 숫자
        if can_go(new_x,new_y,graph[curr_x][curr_y]):
            visited[new_x][new_y]=1
            curr_block_num+=1
            dfs(new_x,new_y)


for i in range(n):
    for j in range(n):
        if visited[i][j]==0 :
            visited[i][j]=1 #방문
            curr_block_num=1
            dfs(i,j)

            if curr_block_num>=4:
                bump_block+=1
            
            max_block=max(max_block,curr_block_num)

            
print(bump_block,max_block)