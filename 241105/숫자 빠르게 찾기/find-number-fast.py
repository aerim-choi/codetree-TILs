n, m =map(int, input().split())

num_list = list(map(int, input().split()))

def binary_search(num_list, left, right, target):
    idx = -1

    while left<=right:
        mid = (left+right)//2

        if num_list[mid] == target:
            idx = mid + 1 
            break
        
        if num_list[mid]> target :
            right = mid - 1
        else:
            left = mid  + 1 
    
    return idx


for _ in range(m):
    target = int(input())

    print(binary_search(num_list,0,n-1,target))