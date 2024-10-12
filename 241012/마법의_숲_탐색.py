from collections import deque
#행, 열, 정령을 입력받는다.
R, C, K = map(int, input().split())

di = [-1,0,1,0]
dj  =[0,1,0,-1]
answer = 0
#북 동 남 서
def draw(curr_i,curr_j,golem_cnt):
    arr[curr_i][curr_j]=golem_cnt
    for i, j in zip(di, dj):
        ni, nj = curr_i + i, curr_j + j
        arr[ni][nj] = golem_cnt

#마법의 숲을 초기화 한다,
arr = [[1]+[0]*C+[1] for _ in range(R+3)]+[[1]*(C+2)]
exit_set = set()
golem_cnt = 2  # 1은 막힌거라 2부터 색칠해야함

def in_range(i,j):
    return 3 <= i < R + 3 and 1 <= j < C+1
def can_go(i,j):
    return 0<=i<R+4 and 0<=j<C+2

def bfs(curr_i, curr_j):
    # 최대 행을 반환해야함
    max_i = 0
    visited = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]

    q = deque()
    q.append((curr_i, curr_j))
    visited[curr_i][curr_j] = 1

    while q:
        si, sj = q.popleft()  # 현재 위치
        max_i = max(si, max_i)

        for i, j in zip(di, dj):
            ni, nj = si + i, sj + j
            # 범위 안에 있고, 방문하지 않았고, 수가 같아야 이동할 수 있음 , 아니면 수가 다른데 출구 인 경우
            if in_range(ni,nj) and visited[ni][nj] == 0 and ((arr[si][sj] == arr[ni][nj]) or (
                 arr[ni][nj] > 1 and ((si,sj) in exit_set))):
                q.append((ni, nj))
                visited[ni][nj] = 1


    #근데 최대행은 -2해줘야함(행 늘려놔서)
    return max_i-2


for i in range(K):
    #골렘이 출발하는 열, 골렘의 출구 방향 정보
    c , d = map(int, input().split())

    #정령의 위치(curr)
    curr_i = 1 #정령은 가운데에 있으니까 1행부터 시작
    curr_j = c #출발하는 열
    curr_d = d #골렘의 출구 정보

    while True :
        # 남쪽으로 이동
        if can_go(curr_i+1,curr_j-1) and can_go(curr_i+2,curr_j) and can_go(curr_i+1,curr_j+1) and arr[curr_i+1][curr_j-1] + arr[curr_i+2][curr_j] + arr[curr_i+1][curr_j+1]==0:
                curr_i+=1

        #서쪽으로 이동
        elif can_go(curr_i-1,curr_j-1) and can_go(curr_i,curr_j-2) and can_go(curr_i+1,curr_j-2) and can_go(curr_i+1,curr_j-1) and can_go(curr_i+2,curr_j-1) and (arr[curr_i-1][curr_j-1] + arr[curr_i][curr_j-2]+ arr[curr_i+1][curr_j-2]+ arr[curr_i+1][curr_j-1]+ arr[curr_i+2][curr_j-1])==0:
                curr_i+=1
                curr_j-=1
                curr_d = (curr_d-1)%4
        #동쪽으로 이동
        elif can_go(curr_i-1,curr_j+1) and can_go(curr_i,curr_j+2) and can_go(curr_i+1,curr_j+1) and can_go(curr_i+1,curr_j+2) and can_go(curr_i+2,curr_j+1) and (arr[curr_i-1][curr_j+1]+ arr[curr_i][curr_j+2]+ arr[curr_i+1][curr_j+1]+ arr[curr_i+1][curr_j+2]+ arr[curr_i+2][curr_j+1])==0:
                curr_i+=1
                curr_j+=1
                curr_d = (curr_d+1)%4


        #이동 불가하면 최종 정령의 인덱스부터 탐색을 한다.
        else:
            break

    #만약 정령의 위치가 4보다 작다면 초기화(삐져나온거임)
    if curr_i<4:
        # 탐색 안해도 됨
        #정령 초기화
        golem_cnt=2
        #마법의 숲 초기화
        arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
        #출구 초기화
        exit_set.clear()
    else:
        draw(curr_i,curr_j,golem_cnt)
        #출구를 담는다.
        exit_set.add((curr_i + di[curr_d], curr_j + dj[curr_d]))
        golem_cnt+=1
        #bfs한다->bfs해서 최대 행을 구한다음 answer에 더해준다.
        max_row = bfs(curr_i,curr_j)
        answer+=max_row


print(answer)
