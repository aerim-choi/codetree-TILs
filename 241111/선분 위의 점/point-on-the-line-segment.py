n, m =map(int,input().split())

dot_arr = list(map(int, input().split()))

dot_arr = sorted(dot_arr)

def in_range(x1,x2,dot):
    if x1<=dot<=x2:
        return True
    else:
        return False

def find(x1,x2):
    
    answer = 0
    for dot in dot_arr:
        if in_range(x1,x2,dot):
            answer+=1
    return answer


for _ in range(m):
    x1 , x2 = map(int,input().split())
    print(find(x1,x2))

