N =int(input())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

#오른쪽 혹은 밑으로 이동해서 N,N으로 간다.
dp =[[0 for _ in range(N)]for _ in range(N)]

def initalize():
    dp[0][0]=array[0][0]

    #오른쪽 채우기

    #아래로 채우기
    for i in range(1,N):
        dp[i][0] = dp[i-1][0] + array[i][0]
    #오른쪽으로 채우기
    for j in range(1,N):
        dp[0][j] = dp[0][j-1] + array[0][j]


initalize()

for i in range(1,N):
    for j in range(1,N):
        dp[i][j] = max(dp[i-1][j]+ array[i][j], dp[i][j-1]+array[i][j])

print(dp[N-1][N-1])