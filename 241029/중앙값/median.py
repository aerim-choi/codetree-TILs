import heapq
t = int(input()) #테스트 케이스의 개수t

#각 테스트 케이스
#수열의 크기m
#수열의 원소가 m개씩
for _ in range(t):
    m = int(input())
    max_heap = [] #왼쪽  
    min_heap = [] #오른쪽
    
    array = list(map(int, input().split()))

    #일단 첫번째 원소를 집어넣어
    heapq.heappush(max_heap, -array[0])
    
    answer = []
    #첫번째 원소는 무조건 출력임
    answer.append(-max_heap[0])

    for i in range(1,len(array)):
        if len(max_heap) - len(min_heap) >=2:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap)- len(max_heap)>=2 : 
            heapq.heappush(max_heap, -heapq.heappop(min_heap)) 

        if i%2==1: #짝수행이면 출력안함
            if -max_heap[0]>array[i]: #left: 3 array[i]=1 
                #두개를 바꿔야함
                left = - heapq.heappop(max_heap)
                right = array[i]

                heapq.heappush(max_heap, -array[i])
                heapq.heappush(min_heap, left)

            else:
                heapq.heappush(min_heap, array[i])

        else: #홀수행이면 중앙값 출력함 
            if array[i]>min_heap[0]: #left: 3 right:6 <-8
                heapq.heappush(min_heap, array[i])
            else:
                heapq.heappush(max_heap, -array[i])
            
            if len(max_heap)>len(min_heap):
                answer.append(-max_heap[0])
            else:
                answer.append(min_heap[0])
        
    
    for num in answer:
        print(num , end=" ")
    print()