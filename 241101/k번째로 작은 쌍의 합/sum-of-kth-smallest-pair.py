import heapq
n, m, k = map(int, input().split())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

array1 = sorted(array1)
array2 = sorted(array2)

#두수의 쌍을 만들기
min_heap = []

cnt = 0
for i in range(n):
    heapq.heappush(min_heap, (array1[i]+array2[0],array1[i], 0))
    
cnt = 0

while min_heap:
    min_sum, min_arr1, min_arr2_idx = heapq.heappop(min_heap)
    heapq.heappush(min_heap,(min_arr1+array2[min_arr2_idx+1], min_arr1, min_arr2_idx+1))
    cnt+=1

    if cnt==k:
        print(min_sum)
        break