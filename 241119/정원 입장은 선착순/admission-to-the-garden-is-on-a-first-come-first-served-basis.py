import heapq
n = int(input()) #사람 수

heap1 = []

for i in range(n):
    a,t = map(int, input().split())
    
    heapq.heappush(heap1,(a,i,t))

wait_time = 0
curr_time = heap1[0][0]
while heap1:
    a,i,t = heapq.heappop(heap1)
    curr_time = curr_time + t

    heap2 = []
    while len(heap1)>0 and heap1[0][0]<=curr_time:
        #순서대로
        a,i,t = heapq.heappop(heap1)
        heapq.heappush(heap2,(i,a,t))
    
    while heap2:
        i,a,t = heapq.heappop(heap2)
        wait_time=curr_time-a
        curr_time +=t 
    

print(wait_time)
    # 10,4,17
    # 20,3,50
    # 25,1,3
    # 100,5,10
    # 105,2,30

    # 제일 a가 작은 사람
    # 10 17
    # time = 0
    # curr = 27
    # 20 3 50
    # 25 1 3

    # curr =30
    # time = 2

    # curr = 80
    # time = 5

    # 100 5 10
    # curr=100
    # time=5

    # curr=140
    # time=10

    

