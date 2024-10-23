N = int(input())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

#(1,3)->(3,1)

dp =[[0 for _ in range(N)]for _ in range(N)]

def initialize():
    dp[0][N-1]=array[0][N-1]

    #왼쪽으로 가기
    for i in range(N-2, -1,-1):
        dp[0][i] = dp[0][i+1]+ array[0][i]

    #아래로 가기
    for i in range(1,N,1):
        dp[i][N-1] = dp[i-1][N-1] + array[i][N-1]

initialize()

for i in range(1,N,1): 
    for j in range(N-2,-1,-1): 
        #왼쪽 혹은 밑으로만 이동 
        dp[i][j]= min(dp[i][j+1], dp[i-1][j])+ array[i][j]


print(dp[N-1][0])