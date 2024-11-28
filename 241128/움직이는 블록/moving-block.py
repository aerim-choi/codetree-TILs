n = int(input())

#최소로 움직이여할 블럭의 수

blocks=[]
for _ in range(n):
    blocks.append(int(input()))

#target값을 구해
target = sum(blocks)//len(blocks)

#모든 원소가 target값과 같아야함
#target보다 많은 블럭을 적은 블록에게 주고 이게 최선임
answer = 0 
for i in range(n):
    for j in range(n):
        
        if i!=j and target > blocks[i] and target<blocks[j]:
            
            send = blocks[j]-target
            take = target-blocks[i]
            
            result = min(send,take)

            blocks[i]+=result
            blocks[j]-=result

            answer+=result

            if blocks[i]==target:
                break

print(answer)
