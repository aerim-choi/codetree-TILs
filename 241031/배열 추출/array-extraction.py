import heapq
n = int(input())

max_heap = []

for _ in range(n):
    x = int(input())

    if x==0:
        if len(max_heap)==0:
            print(0)
        else:
            print(-heapq.heappop(max_heap))
    else :
        heapq.heappush(max_heap, -x)