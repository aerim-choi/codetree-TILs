n = int(input())

arr = list(map(int, input().split()))

answer_list= []
for i in range(n):
    for j in range(i, n):
        temp_list= []
        for k in range(i,j+1):
            temp_list.append(arr[k])

        answer_list.append(temp_list)

answer = 0 

for temp in answer_list:
    average = sum(temp)/len(temp)

    if average in temp:

        answer+=1

print(answer)