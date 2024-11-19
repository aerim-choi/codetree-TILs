n,m = map(int, input().split())

#숫자 dict 
num_d = dict()
#문자 dict
str_d = dict()

for i in range(1,n+1):
    s = input()
    i = str(i)

    num_d[i]= s
    str_d[s] = i

for _ in range(m):
    find = input()

    if find in num_d:
        print(num_d[find])
    else:
        print(str_d[find])