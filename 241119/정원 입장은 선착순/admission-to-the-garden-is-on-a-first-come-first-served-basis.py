import heapq
n = int(input()) #사람 수

heap1 = []

for i in range(n):
    a,t = map(int, input().split())
    
    heapq.heappush(heap1,(a,i,t))

wait_time = 0
curr_time = heap1[0][0]
wait_time_arr= []
while heap1:
    a,i,t = heapq.heappop(heap1)
    wait_time = 0
    if a+t<curr_time:
        curr_time = curr_time
        wait_time = curr_time-a
        wait_time_arr.append(wait_time)
    else:
        curr_time=a+t
        wait_time_arr.append(wait_time)

    heap2 = []
    while len(heap1)>0 and heap1[0][0]<=curr_time:
        #순서대로
        a,i,t = heapq.heappop(heap1)
        heapq.heappush(heap2,(i,a,t))
    
    while heap2:
        i,a,t = heapq.heappop(heap2)
        
        wait_time=curr_time-a
        curr_time +=t 
       
        wait_time_arr.append(wait_time) 

print(max(wait_time_arr))

