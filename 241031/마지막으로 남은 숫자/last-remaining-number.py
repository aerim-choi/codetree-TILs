import heapq

n =int(input())

nums = list(map(int,input().split()))
max_heap = []


for i in range(0,len(nums)):
    heapq.heappush(max_heap, -nums[i])

#2개 이상 남아 있을 때까지 뽑아
while len(max_heap)>1:
    num1 = -heapq.heappop(max_heap)
    num2 = -heapq.heappop(max_heap)

    diff = abs(num1-num2)

    if diff>0:
        heapq.heappush(max_heap, -diff)
    else:
        continue

#마지막에 남아있는 수를 구하자
if max_heap:
    print(-max_heap[0])
else:
    print(-1)