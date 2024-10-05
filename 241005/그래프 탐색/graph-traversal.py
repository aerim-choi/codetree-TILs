def dfs(vertax):
    for curr_v in graph[vertax]:
        if visited[curr_v] == 0 :
            visited[curr_v] = 1
            dfs(curr_v)

N, M =map(int,input().split())
graph=[]
visited = []


for i in range(0,N+1):
    visited.append(0)

for i in range(0,N+1):
    graph.append([])

for i in range(M):
    x,y =map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)

result = 0
for i in range(2,N+1):
    if visited[i]==1:
        result+=1

print(result)