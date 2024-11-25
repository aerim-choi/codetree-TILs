n, k =map(int, input().split())

arr = list(map(int, input().split()))

freq = dict()

for num in arr:
    if num in freq:
        freq[num]+=1
        
    else:
        freq[num]=1


topk=dict()

keys = []
for key, value in freq.items():
    if value in topk:
        topk[value].append(key)
    else:
        topk[value] = [key]
        keys.append(value)

keys = sorted(keys, reverse=True)

for key, value in topk.items():
    topk[key] = sorted(topk[key],reverse=True)

for num in keys:
    if k<=0:
        break
    for answer in topk[num]:
        if k<=0:
            break

        print(answer, end=" ")
        k-=1
        
    
