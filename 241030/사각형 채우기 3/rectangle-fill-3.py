# n=1, answer=2
# n=2 answer=7
# n=3 answer=22

n = int(input())
memo = [-1 for _ in range(n+1)]
if n==1:
    memo[1]=2
elif n==2:
    memo[1]=2
    memo[2]=7
else:
    memo[1]=2
    memo[2]=7
    memo[3]=22

for i in range(4, n+1):
    memo[i] = memo[i-1]*3 + 1

print(memo[-1])