n, m =map(int,input().split())

peoples = list(map(int, input().split()))

answer = 0
k=1
for i in range(0, len(peoples),k):
    if peoples[i]==1 and i+m<len(peoples)-1 and peoples[i+m]==1:
        
        answer+=1
        k= i+(2*m+1)

    else:
        k=1
    
print(answer)