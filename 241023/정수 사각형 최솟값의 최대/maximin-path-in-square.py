N= int(input())

#(1,1)->(N,N)
#오른쪽 혹은 밑으로만 이동

array= []
dp=[[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    array.append(list(map(int, input().split())))

def initialize():
    dp[0][0] = array[0][0]
    #오른쪽으로 이동
    for i in range(1,N):
        dp[0][i]= min(dp[0][i-1],array[0][i])

    #아래쪽으로 이동
    for i in range(1,N):
        dp[i][0] = min(dp[i-1][0], array[i][0])


initialize()


#가는 경로중 무조건 최소값이 있을텐데 그 최소값 중 가장 큰 것은 무엇인가?

for i in range(1,N):
    for j in range(1,N):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]),array[i][j])

print(dp[N-1][N-1])