from collections import deque 
n = int(input())

q = deque()
arr = list(map(int, input().split()))

arr.sort()

for num in arr:
    q.append(num)

#2개씩 뽑은다음에 더해
answer = 0

while q:

    if len(q)==1:
        break

    else:
        num1 = q.popleft()
        num2 = q.popleft()

        answer+=(num1+num2)

        q.append(num1+num2)

print(answer)

