# 격자의 크기 n
# 연속해야 하는 숫자의 수 m
n, m = map(int, input().split())

# 격자 입력
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

#행복한 수열인지 판단하는 방법
def is_happy_sequence(lst):
    max_seq=1
    current_seq=1
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            current_seq+=1
        else:
            current_seq = 1
        max_seq = max(current_seq,max_seq)
    return max_seq



result = 0


# 각행과 각열에서 수열의 수를 구하면 됨
#행 만들기
rows = matrix

cols = []
# 열 만들기
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(matrix[j][i])
    cols.append(temp)


#행복한지 확인하기
for row in rows:
    if is_happy_sequence(row)>=m:
        result+=1

for col in cols:
    if is_happy_sequence(col)>=m:
        result+=1

print(result)