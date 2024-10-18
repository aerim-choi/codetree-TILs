ans = []

def dist(a,b):
    (ax,ay),(bx,by) = a,b
    return abs(ax-bx) + abs(ay-by)

def calc(combination):
    moves = 0
    for i in range(0,len(combination)-1):
        moves += dist(combination[i], combination[i+1])
    return moves


def solve(curr_num_idx, cnt):
    global combination_result
    global combination_num
    global start
    global end
    if curr_num_idx>=len(num_list):
        if cnt==3:
            
            sort_combination_num= sorted(combination_num)
          
            temp = [start]
            for num in sort_combination_num:
                for i in range(N):
                    for j in range(N):
                        if num==graph[i][j]:
                            temp.append((i,j))
            temp.append(end)
            combination_result.append(temp)
        return 
    else:
        #num을 선택했을 경우
        combination_num.append(num_list[curr_num_idx])
        solve(curr_num_idx+1,cnt+1)
        combination_num.pop()
        #num을 선택하지 않았을 경우
        
        solve(curr_num_idx+1,cnt)
        

#그래프에 있는 숫자 리스트 
num_list=[]
combination_num=[]
combination_result=[]
start = (0,0)
end = (0,0)

N = int(input())
graph = []
visited = [[0 for _ in range(N)]for _ in range(N)]
for _ in range(N):
    row = input()
    temp = []
    for i in range(N):
        temp.append(row[i])
    graph.append(temp)


for i in range(N):
    for j in range(N):
        if graph[i][j]!='.' and graph[i][j]!='S' and graph[i][j]!='E':
            num_list.append(int(graph[i][j]))
            graph[i][j] = int(graph[i][j])
        if graph[i][j]=='S':
            start = (i,j)
        
        if graph[i][j]=='E':
            end = (i,j)


if len(num_list)<3: #만약 그래프에 있는 숫자가 3개 미만이라면 -1출력
    print(-1)
else: #동전 3개를 집어갈 수 있는 경우의 수를 구하기
    solve(0,0)
    min_calc_result=100000
    for combination in combination_result:
        min_calc_result = min(min_calc_result, calc(combination))
    print(min_calc_result)