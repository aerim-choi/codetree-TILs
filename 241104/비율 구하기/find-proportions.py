from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()


for _ in range(n):
    color = input()
    if color in sd:
        sd[color] +=1
    else:
        sd[color] = 1


#사전순 출력
for key, value in sd.items():
    print(key, f"{(value/n)*100:.4f}")