from collections import deque
import heapq
n = int(input())

max_heap=[]

q = deque(map(int, input().split()))

#평균값 구하기
def calc(q):
    #가장 작은 숫자 하나를 제외한 평균을 구한다.  
    q.remove(min(q))

    return sum(q)/len(q)

#k개를 삭제해서 남아 있는 정수 중 가장 작은 숫자하나를 제외한 평균을 구한다.
#1<=k<N-2
for k in range(1, n-2+1, 1):

    copy_q = q.copy()

    for i in range(0,k):
        copy_q.popleft() #뽑아
    
    heapq.heappush(max_heap, -calc(copy_q))

print(f"{-max_heap[0]:.2f}")