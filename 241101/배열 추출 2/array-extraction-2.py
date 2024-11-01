import heapq
n = int(input())

array = []

for _ in range(n):
    x = int(input())
    if x==0:
        if len(array):
            value = heapq.heappop(array)
            print(value[1])
        else:
            print(0)
    else:
        heapq.heappush(array,(abs(x), x))