n, k = map(int, input().split()) #n개의 바구니 k구간
arr= [0 for i in range(101)] #바구니의 위치 0<=바구니위치<=100

def find_candy(start,end):
    if start<0:
        start=0
    elif end>100:
        end=100

    candy_num=0
    for i in range(start,end+1):
        if arr[i]>0:
            candy_num+=arr[i]

    return candy_num
        

for _ in range(n):
    candy, basket_location = map(int, input().split())

    arr[basket_location] += candy #단, 같은 위치에 여러 바구니가 놓여 있는 것이 가능하므로 +


answer= 0 
#중심점 c찾기
for i in range(0,101):
    answer = max(answer, find_candy(i-k,i+k))
print(answer)

