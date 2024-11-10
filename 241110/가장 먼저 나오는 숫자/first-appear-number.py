n, m = map(int,input().split())

arr = list(map(int, input().split()))

x_arr=list(map(int,input().split()))

def binary_search(x):
    idx = n
    left = 0
    right = len(arr)-1

    while left<=right:
        mid = (left+right)//2
        if arr[mid]==x:
            idx = min(mid,idx)

        if arr[mid] < x:
            left = mid+1
        else:
            right = mid-1
        
    return idx    
             
for x in x_arr:
    idx= binary_search(x)
    print(idx+1 if idx!=n else -1)