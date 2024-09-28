def move_right(lst):
    for i in range(len(lst)-1, 0,-1):
        lst[i] = lst[i-1]    
    return lst

def rotate(matrix):
    list1_temp = matrix[0][n-1]
    list1 = matrix[0]
    list1 = move_right(list1)

    list2_temp = matrix[1][n-1]
    list2 = matrix[1]
    list2 = move_right(list2)

    list3_temp = matrix[2][n-1]
    list3 = matrix[2]
    list3 = move_right(list3)

    list1[0] = list3_temp
    list2[0]= list1_temp
    list3[0]= list2_temp

    return matrix


n, t = map(int, input().split())

matrix =[]
for i in range(n):
    matrix.append(list(map(int, input().split())))


for i in range(t):
    matrix = rotate(matrix)


for i in range(3):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()