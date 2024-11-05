n, m =map(int, input().split())

nums = list(map(int, input().split())) #n개의 숫자 오름차순


def lower_bound(target):
    left = 0
    right = n-1
    min_idx = n 

    while left<=right:
        mid = (left+right)//2
        
        if nums[mid]>=target:
            min_idx = min(min_idx,mid)
            right = mid - 1
        else:
            left = mid + 1
    return min_idx


def upper_bound(target):
    left = 0
    right = n-1
    min_idx = n

    while left<=right:
        mid= (left+right)//2

        if nums[mid] > target:
            min_idx = min(min_idx,mid)
            right = mid -1
            
        else:
            left = mid+1
    
    return min_idx

for _ in range(m):
    find_num = int(input())

    left = lower_bound(find_num)

    right = upper_bound(find_num)

    print(right-left)