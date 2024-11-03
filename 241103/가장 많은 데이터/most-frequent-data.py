from collections import defaultdict
n = int(input())

d = defaultdict(lambda : 0)

for i in range(n):
    s = input()

    d[s]+=1

print(max(d.values()))