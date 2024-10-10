from collections import deque
n = int(input())
start_x, start_y , end_x,end_y = map(int,input().split())

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]==1:
        return False
    return True
    
    
#최소 이동 횟수-> bfs
q = deque()
visited = [[0 for _ in range(n)]for _ in range(n)]
step = [[0 for _ in range(n)]for _ in range(n)]

def push(x,y,s):
    step[x][y]= s
    visited[x][y]=1
    q.append((x,y))


def bfs():
    dxs= [-2,-2,-1,-1,1,1,2,2] 
    dys= [-1,1,-2,2,-2,2,-1,1]

    while q:
        curr_x ,curr_y = q.popleft()
        for dx,dy in zip(dxs,dys):
            new_x ,new_y = curr_x+dx, curr_y+dy
            if can_go(new_x,new_y):
                push(new_x,new_y,step[curr_x][curr_y]+1)
                 
push(start_x-1,start_y-1,0)
bfs()

if step[end_x-1][end_y-1]==0:
    print(-1)
else:
    print(step[end_x-1][end_y-1])


# x-2 y-1 x-2 y+1
# x-1 y-2 x-1 y+2

# x+1 y-2 x+1 y+2
# x+2 y-1 x+2 y+1

# (0,0) (0,1) (0,2) (0,3) (0,4)
# (1,0) (1,1) (1,2) (1,3) (1,4)
# (2,0) (2,1) (2,2) (2,3) (2,4)
# (3,0) (3,1) (3,2) (3,3) (3,4)
# (4,0) (4,1) (4,2) (4,3) (4,4)