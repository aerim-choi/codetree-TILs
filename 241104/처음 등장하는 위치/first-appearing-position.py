from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

nums = list(map(int, input().split()))

for i in range(0, len(nums)):
    if nums[i] in sd:
        continue
    else:
        sd[nums[i]]= i+1

for key, value in sd.items():
    print(key, value)