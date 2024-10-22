n = int(input())
visited= [False]*(n+1)
answer = []

result = []


def push(answer):
    temp = ''.join(list(map(str,answer)))
    result.append(int(temp))

def choose(curr_num):
    if curr_num > n:
        push(answer)
        return
    
    for i in range(1, n+1):
        if visited[i]==True:
            continue
        visited[i]= True
        answer.append(i)
        choose(curr_num+1)

        answer.pop()
        visited[i]=False
choose(1)

result.sort(reverse=True)
for s in result :
    s =str(s) 
    temp = list(s)
    print(' '.join(temp))