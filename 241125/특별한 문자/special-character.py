arr = list(input())

words = dict()

for s in arr:
    if s in words:
        words[s]+=1
    else:
        words[s]=1

for key, value in words.items():
    if value==1:
        print(key, end="")
        break