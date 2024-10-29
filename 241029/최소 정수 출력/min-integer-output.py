import heapq

n = int(input()) #연산의 개수

min_heap =[] 
for _ in range(n):
    x= int(input())

    #배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거 비어있으면 0
    if x ==0: 
        if len(min_heap)==0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    
    #배열에 자연수 x를 넣는다
    else:
        heapq.heappush(min_heap, x)