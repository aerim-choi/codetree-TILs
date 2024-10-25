n, r, c = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#시작 위치부터 탐색

curr_r=r-1
curr_c=c-1
print(graph[curr_r][curr_c], end=" ")

def in_range(r,c):
    if 0<=r<n and 0<=c<n:
        return True
    else:
        return False

def simulate(r,c):
    
    # 상하좌우
    drs = [-1,1,0,0]
    dcs = [0,0,-1,1]

    max_num=0
    max_pos=(-1,-1)

    find_flag=1
    for dr,dc in zip(drs,dcs):
        new_r, new_c = r+dr, c+dc

        if in_range(new_r, new_c) and graph[r][c]<graph[new_r][new_c]:
            
            max_num = max(max_num, graph[new_r][new_c])
            max_pos = (new_r,new_c) 
            break
    
    if max_num!=0:
        print(max_num, end=" ")
    return max_pos

while True:
    curr_r,curr_c = simulate(curr_r,curr_c)
    if (curr_r,curr_c)==(-1,-1):
        break