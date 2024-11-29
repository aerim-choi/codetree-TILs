n, k = map(int,input().split())

arr = list(map(int, input().split()))

#연속하여 K 개의 숫자를 골랐을 때

max_sum = 0

for i in range(n-k+1):
    temp_sum = 0
    for j in range(i,i+k): 
        temp_sum+=arr[j]
    
    max_sum = max(max_sum, temp_sum)

print(max_sum)
