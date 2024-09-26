#3*3격자내의 최대 동전의 수 구하는 함수
def get_coin(matrix, row_s, row_e, col_s,col_e):
    coin = 0

    for i in range(row_s, row_e+1):
        for j in range(col_s, col_e+1):
            coin += matrix[i][j]

    return coin

N= int(input())

matrix = []
max_coin = 0
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)


for i in range(0,N-2):
    for j in range(0, N-2):
        max_coin = max(max_coin, get_coin(matrix, i, i+2, j, j+2))

print(max_coin)