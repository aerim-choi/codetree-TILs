n = int(input()) #n명의 사람

arr = []

def find_picture_size(start,end):
    if start<0:
        start=0
    if end>n-1:
        end=n-1
    g_num = 0
    h_num = 0
    for i in range(start,end+1):
        if arr[i][1]=='G':
            g_num+=1
        elif arr[i][1]=='H':
            h_num+=1
    
    if g_num >0 and h_num==0:
        return arr[end][0]-arr[start][0]
    if g_num==0 and h_num>0:
        return arr[end][0]-arr[start][0]
    if g_num==h_num:
        return arr[end][0]-arr[start][0]
    else:
        return 0

if n==1: #사람이 1명뿐인 경우에는 사진의 크기는 0
    print(0)
else:
    for _ in range(n):
        location, alphabet = map(str, input().split())

        location = int(location)

        arr.append([location,alphabet])

    arr.sort(key = lambda x:x[0])

    answer=0

    for i in range(n):
        for k in range(1, n):
            answer= max(answer, find_picture_size(i,i+k))

    print(answer)