n = int(input())
visited= [False]*(n+1)
answer = []

result = []


def push(answer):
    temp = ''.join(list(map(str,answer)))
    result.append(int(temp))

def choose(curr_num):
    if curr_num == 0:
        push(answer)
        return
    
    for i in range(n, 0, -1):
        if visited[i]==True:
            continue
        visited[i]= True
        answer.append(i)
        choose(curr_num-1)

        answer.pop()
        visited[i]=False
choose(n)

for s in result :
    s =str(s) 
    temp = list(s)
    print(' '.join(temp))