arr = list(input())

words = dict()

for s in arr:
    if s in words:
        words[s]+=1
    else:
        words[s]=1

flag = False
for s in arr:
    if words[s]==1:
        print(s)
        flag=True
        break
if flag==False:
    print(None)