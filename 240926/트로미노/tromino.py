#일자 블럭 점수 구하기
def get_oneline_block(lst):
    return sum(lst)
#계단 블럭 점수 구하기
def get_step_block(lst):
    return sum(lst)-min(lst)

n,m = map(int,(input().split()))

matrix=[]
for _ in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

max_type1_block=0 # 가로 일자 블럭 최댓값 

#type1: 가로 일자 블럭
for i in range(n):
    for j in range(0,m-2):
        max_type1_block= max(max_type1_block, get_oneline_block([matrix[i][j],matrix[i][j+1],matrix[i][j+2]]))

#type2: 세로 일자 블럭
max_type2_block=0
for i in range(m):
    for j in range(0,n-2):
        max_type2_block=max(max_type2_block, get_oneline_block([matrix[j][i],matrix[j+1][i],matrix[j+2][i]]))    

#type3: 사각형 블럭
#일단 사각형 한다음에 사각형안에 최소숫자를 빼면 된다.
max_type3_block=0
for i in range(n-1):
    for j in range(m-1):
        max_type3_block= max(max_type3_block,get_step_block([matrix[i][j],matrix[i+1][j],matrix[i][j+1],matrix[i+1][j+1]]))

print(max(max_type1_block,max_type2_block,max_type3_block))