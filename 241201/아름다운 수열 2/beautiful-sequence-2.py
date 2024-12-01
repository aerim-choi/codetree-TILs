n, m =map(int, input().split())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

#순서가 바뀌면 아름다운 수열
def is_beautiful_list(arr):
    arr.sort()
    b_arr.sort()
    for i in range(len(arr)):
        if arr[i]!=b_arr[i]:
            return False
    return True
        

answer=0
for i in range(n-m+1):
    arr = a_arr[i:i+m]
    
    if is_beautiful_list(arr):
        answer+=1

print(answer)
