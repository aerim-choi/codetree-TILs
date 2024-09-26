# 격자의 크기 n
# 연속해야 하는 숫자의 수 m
n, m = map(int, input().split())

# 격자 입력
matrix = []
for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

# print(matrix)
result = 0
# 각행과 각열에서 수열의 수를 구하면 됨
#행이 연속하는가?
rows = matrix

cols = []
#열이 연속하는가?
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(matrix[j][i])
    cols.append(temp)

for row in rows:
    #m만큼 연속인가?
    flag=0
    for i in range(len(row)):
        if (i+m-1) < len(row):
            for j in range(i+1,i+m):
                if row[i] == row[j]:
                    if flag==0:
                        result+=1
                        flag=1
                break

# print(cols)
for col in cols:
    #m만큼 연속인가?
    flag=0
    for i in range(len(col)):
        if (i+m-1) < len(col):
            for j in range(i+1,i+m):
                if col[i] == col[j]:
                    if flag == 0:
                        result+=1
                        flag=1
                break

print(result)