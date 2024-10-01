n= int(input())

line = []
for i in range(n):
    x1, x2 = map(int, input().split())
    line.append((x1,x2))

vertical = []

for i in range(0,1001):
    vertical.append(0)

line.sort(key= lambda x:(x[1]-x[0]))

answer= 0 
for x1,x2 in line:

    flag = True
    for i in range(x1,x2+1):
        if vertical[i] == 1: #하나라도 겹치는게 있으면 
            flag = False
            break
    
    if flag==True:
        for i in range(x1,x2+1):
            vertical[i]=1
        answer+=1

print(answer)