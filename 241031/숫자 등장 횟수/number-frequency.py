n, m = map(int, input().split())

array = list(map(int, input().split()))

find_num = list(map(int, input().split()))

d = dict()

for num in array:
    if num in d:
        d[num]+=1
    else:
        d[num]=1

for num in find_num:
    if num in d:
        print(d[num], end=" ")
    else:
        print(0, end = " ")