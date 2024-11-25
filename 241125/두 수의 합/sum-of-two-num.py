n, k = map(int, input().split())

arr = list(map(int, input().split()))

count = dict()
answer = 0
for i in range(n):
    diff = k-arr[i]

    if diff in count:
        answer+=count[diff]
    
    if arr[i] in count:
        count[arr[i]]+=1
    else:
        count[arr[i]]=1

print(answer)