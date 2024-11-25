n, k =map(int, input().split())

arr = list(map(int, input().split()))

freq = dict()

max_key= 0
max_value=0

for num in arr:
    if num in freq:
        freq[num]+=1

        if max_value < freq[num]:
            max_value = freq[num]
            max_key = num
        
    else:
        freq[num]=1

        if max_key < num:
            max_key=num
            max_value=1


arr = sorted(arr)
answer = []
for num in arr:
    if num == max_key:
        answer.append(num)
        break
    if freq[num] == max_value:
        if num not in answer:
            answer.append(num)

answer = sorted(answer, reverse=True)
for i in answer:
    print(i, end=" ")