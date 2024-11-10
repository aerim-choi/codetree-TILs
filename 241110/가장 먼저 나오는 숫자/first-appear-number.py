n, m = map(int,input().split())

arr = list(map(int, input().split()))

x_arr=list(map(int,input().split()))

def binary_search(x):
    idx = -1
    left = 0
    right = len(arr)-1

    while left<=right:
        mid = (left+right)//2
        if arr[mid]==x:
            idx = mid

        if arr[mid] < x:
            left = mid+1

        else:
            right = mid-1
    return idx    
             
for x in x_arr:
    idx= binary_search(x)
    if idx==-1:
        print(-1)
    else:
        print(idx+1)