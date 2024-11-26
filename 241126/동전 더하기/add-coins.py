n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
coins= sorted(coins, reverse=True)

answer= 0 

while k>0:

    for coin in coins:
        answer += (k // coin)
        k = k%coin

        if k ==0 :
            break

print(answer)