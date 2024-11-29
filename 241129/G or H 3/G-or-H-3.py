n, k = map(int,input().split()) #n명의 사람, 사진의 크기k

arr = [0]*10001
location_list = []
for _ in range(n):
    location, alphabet = map(str, input().split())
    location = int(location)
    if alphabet =='G':
        arr[location] = 1
    else:
        arr[location] = 2
    
#최대값 구하기
answer = 0 
for i in range(1, 10001-k+1):
    temp_max = 0
    if arr[i]!=0:
        for j in range(i,i+k+1): 
            temp_max+=arr[j]
        
        answer = max(temp_max,answer)

print(answer)