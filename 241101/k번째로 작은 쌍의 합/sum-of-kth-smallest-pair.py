import heapq
n, m, k = map(int, input().split())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

#두수의 쌍을 만들기
min_heap = []

for i in range(n):
    for j in range(m):
        heapq.heappush(min_heap, (array1[i]+array2[j],array1[i],array2[j]))

print(min_heap[k-1][0])