n = int(input())
5
5 -2
5 -3
#[-1 -1 -1 -1 1 1 -1 -1]
memo = [-1 for _ in range(n+1)]

if n<3:
    #점화식을 채우기 위해서는 아직 오르지 않은 최초의 상태(dp[0])도 한가지의 가짓수가 있다고 판단해야함
    memo[0]=1 
    memo[1]=0
    memo[2]=1
else:
    memo[0]=1 
    memo[1]=0
    memo[2]=1
    memo[3]=1

def dp(n):
    if memo[n]!=-1:
        return memo[n]
    if n<0:
        return 0
    
    memo[n] = dp(n-3) + dp(n-2)
    return memo[n]

dp(n)
#n층 높이의 계단에 올라가기 위한 서로 다른 방법의 수를 10,007로 나눈 나머지 출력

print(memo[n]%10007)