n, m =map(int, input().split())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

#순서가 바뀌면 아름다운 수열
def is_beautiful_list(arr):
    b_arr_set = set(b_arr)
    arr_set = set(arr)

    if (b_arr_set&arr_set)==arr_set:
        return True
    else:
        return False

answer=0
for i in range(n-m+1):
    arr = a_arr[i:i+m]
    
    if is_beautiful_list(arr):
        answer+=1

print(answer)
