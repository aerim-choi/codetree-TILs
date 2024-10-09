from collections import deque

def search_go(x,y,num):
    if x<0 or x>=n or y<0 or y>=n: #격자를 벗어날 경우 갈 수 없음
        return False
    if graph[x][y] >= num: #시작위치보다 작아야 갈 수 있음
        return False
    if visited[x][y]==1: #방문했을 경우 갈 수 없음
        return False
    return True

def bfs(num):
    #상하좌우
    dxs=[0,0,-1,1]
    dys=[1,-1,0,0]
    flag=1
    #시작위치로 부터 상하좌우 인접한 곳을 탐색한다.
    while q:
        curr_x, curr_y = q.popleft()
        for x,y in zip(dxs,dys):
            new_x, new_y = curr_x+x , curr_y+y
            if search_go(new_x,new_y,num):
                flag+=1
                visited[new_x][new_y]=1
                q.append((new_x,new_y))

    if flag==1:
        return False


def find_max_xy(num):
    #우선순위1:상하좌우에서 제일 최댓값
    #visited에서 1인 곳에서 최댓값을 고른다.
    max_num = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1 and graph[i][j]!=num:
                max_num = max(max_num, graph[i][j])
    
    #우선순위2:최댓값이 같을 경우에는 행번호가 가장 작은 곳으로 이동
    #우선순위3:행번호가 같을 경우에는 열번호가 가장 작은 곳으로 이동
    #이중 for문에서 제일 빠르게 최댓값이 나오는 곳을 고른다. 
    max_i=0
    max_j=0
    find_flag=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1 and max_num == graph[i][j]:
                max_i=i
                max_j=j
                find_flag=1
                break
        if find_flag==1:
            break
    
    return [max_i,max_j] #위치값을 리턴한다.(다음 탐색할 r,c)
                

    

n,k = tuple(map(int, input().split())) #격자의 크기 n, 반복할 횟수 k

graph = [] # 문제에서 주어진 정보를 담는 2차원 배열
for i in range(n):
    graph.append(list(map(int,input().split())))



#시작위치(r,c)를 queue에 담는다
r,c=tuple(map(int,input().split()))

for i in range(k):
    #bfs 탐색을 하기위해 queue를 생성
    q = deque()
    #방문한 정보를 담는 2차원 배열
    visited = [[0 for _ in range(n)]for _ in range(n)]
    visited[r-1][c-1]=1 #방문
    q.append((r-1,c-1)) #큐에 추가
    #탐색이 안되면 멈추고 r,c리턴 
    
    if bfs(graph[r-1][c-1])==False:
        break
    else:
        t=find_max_xy(graph[r-1][c-1])
        r= t[0]+1
        c= t[1]+1
  

print(r,c)