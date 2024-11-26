import heapq
n = int(input())

arr = list(map(int, input().split()))

#2개씩 계속 뽑아 
#근데 계속 min값을 구해야하니까 최소힙으로 하면됨
answer = 0 
heapq.heapify(arr)

while len(arr)>1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)

    answer = a+b
    heapq.heappush(arr,a+b)

while arr:
    answer += heapq.heappop(arr)

print(answer)

