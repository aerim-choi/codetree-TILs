n= int(input())

jenga = []

for _ in range(n):
    jenga.append(int(input()))

pick = []

for _ in range(2):
    #근데 순서는 인덱스+1임
    pick.append(tuple(map(int,input().split())))

end_of_array=n

#탐색
for s,e in pick:
    temp = []
    
    end_of_temp_array=0

    #뺀 부분 0으로 만든다
    for i in range(s-1,e):
        jenga[i]=0
    
    #0인 부분을 빼고 temp에 넣는다.
    for i in range(end_of_array):
        if jenga[i]!=0:
            temp.append(jenga[i])
            end_of_temp_array+=1

    for i in range(end_of_temp_array):
        jenga[i]=temp[i]

    end_of_array= end_of_temp_array


if end_of_array==0:
    print(0)
else:
    print(end_of_array)
    for i in range(end_of_array):
        print(jenga[i])