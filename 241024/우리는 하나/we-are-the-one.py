from collections import deque

#격자의 크기 n
#고를 도시의 수 k
#두 도시간의 높이 차가 u이상 d이하

n,k,u,d = map(int, input().split())
graph = []
q = deque()
for _ in range(n):
    graph.append(list(map(int, input().split())))

#k개의 도시 조합을 만들기 위해 위치 인덱스를 저장
city_list = []
for i in range(n):
    for j in range(n):
        city_list.append((i,j))

answer= [] 
max_result = 0 

#city_list에서 k 개의 도시를 고른다.
def choose(cnt, curr_idx):
    if cnt>k:
        #선택된 k개의 도시를 먼저 queue에 집어넣는다.
        for elem in answer:
            q.append(elem)
        #bfs탐색
        global max_result
        result =bfs()

        max_result= max(max_result, result)

        return 
    if curr_idx == len(city_list):
        return
    #현재 graph[idx]를 뽑았을 때
    answer.append(city_list[curr_idx])
    choose(cnt+1, curr_idx+1)
    answer.pop()

    #현재 graph[idx]를 뽑지 않았을 때
    choose(cnt, curr_idx+1)
#상하좌우
dr=[-1,1,0,0]
dc=[0,0,-1,1]
def in_range(r,c):
    if 0<=r<n and 0<=c<n:
        return True
    else: 
        return False

def bfs():
    visited = [[0 for _ in range(n)] for _ in range(n)]

    while q:
        curr_r, curr_c = q.popleft()
        visited[curr_r][curr_c] = 1
        
        for r,c in zip(dr,dc):
            new_r, new_c = curr_r + r , curr_c +c
            if in_range(new_r,new_c) and visited[new_r][new_c]==0 and u<=abs(graph[curr_r][curr_c]- graph[new_r][new_c])<=d:
                visited[new_r][new_c]=1
                q.append((new_r,new_c))
    cnt=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1:
                cnt+=1
    return cnt

choose(1, 0)
print(max_result)