import heapq 

heap = []
n = int(input())

car_price_list = list(map(int, input().split()))

answer = 0 #최대이익 

heapq.heappush(heap, car_price_list[0])
for i in range(0, len(car_price_list)):
    #현재값 - 최소 
    diff = car_price_list[i]-heap[0]

    answer = max(answer,diff)

    heapq.heappush(heap, car_price_list[i])
    

print(answer)