import heapq

n = int(input())

arr = list(map(int, input().split()))

print(-1)
print(-1)


def find_min(arr):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap,num)

    #최솟값 3개
    answer = 1

    for _ in range(3):
        answer = answer * heapq.heappop(min_heap)
    return answer
    

for i in range(2,len(arr)):
    print(find_min(arr[0:i+1]))
