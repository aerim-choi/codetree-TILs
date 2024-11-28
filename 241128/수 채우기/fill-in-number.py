n = int(input())

answer = 0

#일단 5원짜리가 최대 몇개 필요한지 알아본다.
max_coin_5 = n//5

#이후 5원의 개수를 줄이면서 알아본다
for coin_5 in range(max_coin_5,-1,-1):
    temp_answer=0
    temp_answer += coin_5 #5원의 개수를 더한다.
    copy_n = n 

    copy_n = copy_n - (5 * coin_5)

    if copy_n%2==0:
        temp_answer += copy_n//2
        answer = temp_answer
        break
    else:
        continue

print(answer)
