n, k = map(int, input().split()) #n개의 바구니 k구간
arr= [0 for i in range(101)] #바구니의 위치 0<=바구니위치<=100

def find_candy(start,end):
    if start<1:
        start=1
    elif end>100:
        end=100
    
    candy_num=0
    for i in range(start,end+1):
        if arr[i]>0:
            candy_num+=arr[i]
    
    return candy_num
        

for _ in range(n):
    candy, basket_location = map(int, input().split())

    arr[basket_location]=candy

answer= 0 
#중심점 c찾기
for i in range(1,101):
    answer = max(answer, find_candy(i-k,i+k))
print(answer)

