from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    animal = input()
    if animal in sd:
        sd[animal]+=1
    else:
        sd[animal]=1

for key, value in sd.items():
    print(key, value)