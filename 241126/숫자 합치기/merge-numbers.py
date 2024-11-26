n = int(input())

arr = list(map(int, input().split()))

arr.sort()

#2개씩 계속 뽑아 

pair_arr = []
answer = 0 

while arr:

    if len(arr)==1: #홀수개 일 수도 있으므로 
        pair_arr.append(arr.pop(0))
    else:
        num1= arr.pop(0)
        num2= arr.pop(0)
        pair_arr.append(num1+num2)
        answer += num1+num2



while pair_arr:
    if len(pair_arr)==1:
        answer+=pair_arr.pop(0)
    else:
        answer+=pair_arr.pop(0)+pair_arr.pop(0)

print(answer)

