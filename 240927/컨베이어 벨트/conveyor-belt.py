def rotate(up, down):
    #윗줄은 오른쪽으로 
    up_temp = up[len(up)-1] #유실되는 위에 숫자
    for i in range(n-2,-1,-1):
        up[i+1] = up[i]

    #아랫줄은 왼쪽으로
    down_temp = down[0] #유실되는 아래 숫자
    for i in range(1,n):
        down[i-1]=down[i]

    up[0]=down_temp
    down[len(up)-1]= up_temp
    

n, t = map(int, input().split())

up = list(map(int, input().split()))
down = list(map(int, input().split()))
down.reverse()


for i in range(t):
    rotate(up,down)

down.reverse()

for i in range(n):
    print(up[i], end=" ")

print()
for i in range(n):
    print(down[i], end=" ")