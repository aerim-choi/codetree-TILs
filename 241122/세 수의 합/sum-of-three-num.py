n, k = map(int, input().split())

arr = list(map(int, input().split()))

count = dict()
ans=0

for i in range(0, len(arr)-1):
    for j in range(i+1,len(arr)):
        diff = k-(arr[i] +arr[j])

        if diff in count:
            ans += count[diff]
        
    if arr[i] in count:
        count[arr[i]]+=1
    else:
        count[arr[i]]=1

print(ans)