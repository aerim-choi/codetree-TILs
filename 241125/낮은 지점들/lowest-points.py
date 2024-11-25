n= int(input())

dot = dict()
for _ in range(n):
    x, y = map(int, input().split())

    if x in dot:
        dot[x]= min(dot[x], y)
    else:
        dot[x]=y

answer=0
for value in dot.values():
    answer+=value

print(answer)