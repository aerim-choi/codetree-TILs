n = int(input())


dp = []
dp.append(1)
dp.append(1)

for _ in range(3,n+1):
    dp.append(dp[-2]+dp[-1])

print(dp[-1])