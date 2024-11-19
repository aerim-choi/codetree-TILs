import heapq

n = int(input())

arr = list(map(int, input().split()))

min_heap=[]

for num in arr:
    heapq.heappush(min_heap,num)

    if len(min_heap)<3:
        print(-1)
    else:
        a= heapq.heappop(min_heap)
        b= heapq.heappop(min_heap)
        c= heapq.heappop(min_heap)

        print(a*b*c)

        heapq.heappush(min_heap,a)
        heapq.heappush(min_heap,b)
        heapq.heappush(min_heap,c)