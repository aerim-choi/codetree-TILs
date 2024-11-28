n = int(input())

#최소로 움직이여할 블럭의 수

blocks=[]
for _ in range(n):
    blocks.append(int(input()))

#target값을 구해
target = sum(blocks)/len(blocks)

#모든 원소가 target값과 같아야함
#target보다 많은 블럭을 적은 블록에게 주고 이게 최선임
answer = 0 
for i in range(n-1):
    for j in range(i+1, n):
        if target > blocks[i] and target<blocks[j]:
            
            give = blocks[j]-target
            send = blocks[i]-target 
            
            result = min(give,send)

            blocks[i]+=result
            blocks[j]-=result
            answer+=result

        if blocks[i]==target:
            break
        else:
            continue