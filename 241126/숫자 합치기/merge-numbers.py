n = int(input())

arr = list(map(int, input().split()))

arr.sort()

#2개씩 뽑은다음에 더해
answer = 0

prev = 0 
while arr:

    if len(arr)==1:
        break

    else:
        num1 = arr[0]
        num2 = arr[1]

        answer+= prev+ (arr[0]+arr[1])
        prev = arr[0]+arr[1]
       
print(answer)

