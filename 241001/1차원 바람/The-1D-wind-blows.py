#위로 가는거
def check_blow(wind1, wind2):
    for i in range(M):
        if wind1[i]==wind2[i]:
            return True
    return False

#바람 왼쪽 붐
def left_blow_wind(wind_raw):

    wind_temp = wind_raw[M-1]

    for i in range(M-1,0,-1):
        wind_raw[i] = wind_raw[i-1]

    wind_raw[0] = wind_temp

#바람 오른쪽 붐
def right_blow_wind(wind_raw):
    if raw <0 or raw > N: 
        return

    wind_temp = wind_raw[0]

    for i in range(1,M):
        wind_raw[i-1] = wind_raw[i] 

    wind_raw[M-1] = wind_temp

#행렬의 크기 N, M 바람이 불어온 횟수 Q
N,M,Q = map(int, input().split())

wind_matrix=[]
for i in range(N):
    wind_raw = list(map(int,input().split()))
    wind_matrix.append(wind_raw)

wind_directions=[]
for i in range(Q):
    raw, direction = input().split()
    wind_directions.append((int(raw),direction))


for (raw,direction) in wind_directions:
    if direction=='L':
        left_blow_wind(wind_matrix[raw-1])
        flag = 'R'    
        #위로 전파 여부
        for i in range(raw-1, 0, -1):
            if check_blow(wind_matrix[i],wind_matrix[i-1])==False:
                break
            else: 
                if flag=='R':
                    right_blow_wind(wind_matrix[i-1])
                    flag='L'
                else:
                    left_blow_wind(wind_matrix[i-1])
                    flag='R'

        flag = 'R' 
        #아래 전파 여부
        for i in range(raw-1, N-1, 1):
            if check_blow(wind_matrix[i], wind_matrix[i+1])==False:
                break
            else:
                if flag=='R':
                    right_blow_wind(wind_matrix[i+1])
                    flag='L'
                else:
                    left_blow_wind(wind_matrix[i+1])
                    flag='R'

    else: #'R'
        right_blow_wind(wind_matrix[raw-1])
        flag = 'L' 
        #위로 전파 여부
        for i in range(raw-1, 0, -1):
            if check_blow(wind_matrix[i],wind_matrix[i-1])==False:
                break
            else:
                print(wind_matrix[i-1])
                if flag=='R':
                    right_blow_wind(wind_matrix[i-1])
                    flag='L'
                else: 
                    left_blow_wind(wind_matrix[i-1])
                    flag='R'

        flag = 'L' 
        #아래 전파 여부
        for i in range(raw-1, N-1, 1):
            if check_blow(wind_matrix[i], wind_matrix[i+1])==False:
                break
            else:
                print("hello:",wind_matrix[i+1])
                if flag=='R':
                    right_blow_wind(wind_matrix[i+1])
                    flag='L'
                else: 
                    left_blow_wind(wind_matrix[i+1])
                    flag='R'



for wind in wind_matrix:
    for elem in wind:
        print(elem, end=" ")
    print()