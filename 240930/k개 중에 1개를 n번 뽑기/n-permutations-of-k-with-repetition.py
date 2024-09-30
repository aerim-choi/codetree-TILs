K, N = map(int, input().split())

def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()

answer = []
def chooseNum(curr_idx):
    if curr_idx > N:
        print_answer()
        return
    else:
        for i in range(1,K+1):
            answer.append(i)
            chooseNum(curr_idx+1)
            answer.pop()

        return

chooseNum(1)