import heapq

n,m = map(int, input().split())

numbers = list(map(int, input().split()))
max_heap = []

#초기 리스트 생성
for i in range(len(numbers)):
    heapq.heappush(max_heap, -numbers[i])


for _ in range(m):
    #최대값을 pop하고 -1해서 다시집어넣음
    value = - heapq.heappop(max_heap)
    value = value-1

    heapq.heappush(max_heap, -value)

print(-max_heap[0])