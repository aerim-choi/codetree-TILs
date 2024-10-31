import heapq
n = int(input())
nums = list(map(int, input().split()))

num_sum= nums[len(nums)-1]
min_heap = []
heapq.heappush(min_heap, (nums[len(nums)-1]))

max_avg = -1

#K개를 삭제한다
for i in range(n-2, 0,-1): 
    num_sum += nums[i]
    heapq.heappush(min_heap,nums[i])

    avg = (num_sum - min_heap[0]) / (n - i -1)

    max_avg = max(max_avg, avg)


print(f"{max_avg:.2f}")