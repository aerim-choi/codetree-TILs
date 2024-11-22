n, k = map(int, input().split())

arr = list(map(int, input().split()))

answer=0
for i in range(0,len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i]+ arr[j]==k:
            answer+=1

print(answer)