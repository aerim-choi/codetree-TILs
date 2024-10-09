import sys
sys.setrecursionlimit(10**4)

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

#방문정보를 담을 2차원 배열
visited = [[0 for _ in range(n)]for _ in range(n)]

#방문한 블럭의 숫자정보를 담을 배열
block_set = set()

# 터지게 되는 블럭의 수와 최대 블럭의 크기
bump_block = 0
max_block = 0
bump_visited = [[0 for _ in range(n)]for _ in range(n)]

# 블럭을 이루고 있는 칸의 수가 4개 이상의 경우 터짐
def check_visited(a,b):
    global bump_block
    global max_block
    block_cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1 :
                block_cnt+=1
    
    if block_cnt>=4:
        bump_block+=1
        
        for i in range(n):
            for j in range(n):
                if visited[i][j]==1:
                    bump_visited[i][j]=visited[i][j]
    
    max_block = max(max_block, block_cnt)


def dfs(curr_x,curr_y):
    visited[curr_x][curr_y]=1 #방문
    
    for x,y in [(0,1),(0,-1),(-1,0),(1,0)]:
        new_x, new_y = curr_x+x , curr_y+y
    
        # 매트릭스를 벗어나지 않았는지, 방문하지 않았는지, 같은 숫자
        if not (new_x<0 or new_x>=n or new_y<0 or new_y>=n) and visited[new_x][new_y]==0 and graph[curr_x][curr_y]==graph[new_x][new_y]:
            visited[new_x][new_y]=1
            dfs(new_x,new_y)





for i in range(n):
    for j in range(n):
        if bump_visited[i][j]==0:
            dfs(i,j)
            check_visited(i,j)  
            visited = [[0 for _ in range(n)]for _ in range(n)]

            
print(bump_block,max_block)