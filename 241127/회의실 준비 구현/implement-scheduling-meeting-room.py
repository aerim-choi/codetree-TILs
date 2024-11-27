n = int(input())

rooms=[]
for _ in range(n):
    start, end = map(int, input().split())

    rooms.append((start,end))

rooms = sorted(rooms, key = lambda x:x[1])

answer = 0

curr_time = 0
for room in rooms:
    if curr_time<=room[0]:
        curr_time=room[1]
        answer+=1
    else:
        continue
        
print(answer)