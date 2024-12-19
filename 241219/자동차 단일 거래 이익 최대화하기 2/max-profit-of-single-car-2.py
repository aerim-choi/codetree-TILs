n = int(input())

car_price_list = list(map(int, input().split()))

answer = -1 #최대이익 

for i in range(len(car_price_list)-1, 0, -1):
    for j in range(i-1, -1, -1):
        diff = car_price_list[i]-car_price_list[j]
   
        answer=max(diff, answer)

print(answer)