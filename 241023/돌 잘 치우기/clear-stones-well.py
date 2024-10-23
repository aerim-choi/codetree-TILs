from collections import deque
#n*n격자
#m개의 돌 치운다
#k개의 시작점으로 부터 상하좌우로 이동
n,m,k= map(int,(input().split()))

array=[]

#그래프 입력받기
for _ in range(n):
    array.append(list(map(int, input().split())))


start_v = []
#시작점 입력받기
for _ in range(m):
    r,c = map(int,input().split())
    start_v.append((r-1,c-1))

#일단 돌을 치울 조합들을 찾는다. 돌이 있는 곳을 탐색
def find_doll():
    doll_list = []

    for i in range(n):
        for j in range(n):
            if array[i][j]==1:
                doll_list.append((i,j))

    return doll_list


def in_range(r,c):
    if 0<=r<n and 0<=c<n:
        return True
    else:
        return False
#doll_list에서 k개의 조합을 뽑는 함수 

answer= []

#상하좌우
dr = [1,-1,0,0]
dc = [0,0,-1,1]
max_cnt = 0
def choose(curr_num, idx, doll_list,array):
    if curr_num>k:
        #여기서 돌을 치우는 거임 
        copy_array = [x[:] for x in array]
        for r,c in answer:
            copy_array[r][c]=0
        #bfs탐색 시작
        q = deque() 
        visited = [[0 for _ in range(n)] for _ in range(n)]
        for sr,sc in start_v:
            q.append((sr,sc)) 
        while q:
            curr_r , curr_c = q.popleft()
            visited[curr_r][curr_c]=1
            for r,c in zip(dr,dc):
                new_r,new_c = curr_r+r, curr_c+c
                if in_range(new_r,new_c) and visited[new_r][new_c]==0 and copy_array[new_r][new_c]==0:
                    
                    visited[new_r][new_c]=1
                    q.append((new_r,new_c))
                    
        
        global max_cnt
        cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j]==1:
                    cnt+=1
       
        max_cnt= max(max_cnt,cnt)

        
    else:
        if idx==len(doll_list):
            return
        #뽑는경우
        answer.append(doll_list[idx])
        choose(curr_num+1, idx+1, doll_list,array)
        answer.pop()
        
        #안뽑는 경우
        choose(curr_num, idx+1, doll_list,array)



#main코드
doll_list = find_doll()
choose(1,0,doll_list,array)

print(max_cnt)