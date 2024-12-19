n = int(input())

car_price_list = list(map(int, input().split()))

answer = 0 #최대이익 

for i in range(len(car_price_list)-1, 1, -1):
        
        diff = car_price_list[i] - min(car_price_list[0:i-1])
    
        answer=max(diff, answer)

print(answer)