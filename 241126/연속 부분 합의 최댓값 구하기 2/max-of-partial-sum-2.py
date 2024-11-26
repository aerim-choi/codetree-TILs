n = int(input())

arr = list(map(int, input().split()))

answer = -1001 #max값
total = arr[0]
for i in range(1,len(arr)):
    if total<0:
        total = arr[i]
    else:    
        total += arr[i]
    
  
    answer = max(answer, total)
print(answer)
