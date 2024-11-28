n, m =map(int,input().split())

peoples = list(map(int, input().split()))


answer = 0
k=0
while k<n:
    if peoples[k]==1:
        answer+=1
        k+=(2*m)+1
    else:
        k+=1

print(answer)