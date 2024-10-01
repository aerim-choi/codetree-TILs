K,N = map(int, input().split())

def print_num(lst):
    for i in lst:
        print(i, end=" ")
    print()

answer = []
def choose(curr_num):
    if curr_num > N :
        print_num(answer)
        return
    else:
        for i in range(1,K+1,1):
            if len(answer)>=2 and answer[-1]==i and answer[-2]==i:
                continue
            else:
                answer.append(i)
                choose(curr_num+1)
                answer.pop()

choose(1)