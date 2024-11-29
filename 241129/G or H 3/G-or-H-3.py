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
    location_list.append(location)
    
#최대값 구하기
answer = 0 
for location in location_list:
    end= 0
    temp_answer = 0  
    if location+k+1<10001:
        end=location+k+1
    else:
        end=10001  
    for i in range(location,end):
        temp_answer += arr[i]

    answer = max(temp_answer,answer)

print(answer)