n = int(input())
5
5 -2
5 -3

answer = 0
def dp(n):
    if n==0:
        global answer
        answer+=1
        return
    if n<=0:
        return
    #3계단 내려가
    dp(n-3)
    #2계단 내려가
    dp(n-2)

dp(n)

#n층 높이의 계단에 올라가기 위한 서로 다른 방법의 수를 10,007로 나눈 나머지 출력
print(answer%10007)