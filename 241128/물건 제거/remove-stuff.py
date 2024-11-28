n = int(input())

a_arr =list(map(int, input().split()))

k = int(input())

b_arr = list(map(int, input().split()))

a_arr.sort()
b_arr.sort()

#모든 물건 제거 불가능할 경우
if max(a_arr)<max(b_arr):
    print(-1)

#제거 못하는 기계 삭제
for a in a_arr:
    if a<min(b_arr):
        a_arr.remove(a)

answer=0
#a의 개수만큼 끊어서 보기

i=0
while i<len(b_arr):
    arr = b_arr[i:i+len(a_arr)]
    
    count = 0

    for j in range(0,len(arr)):
        if a_arr[j]>=arr[j]:
            count+=1

    i+=count
    answer+=1

print(answer)