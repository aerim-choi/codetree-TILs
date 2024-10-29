import heapq
n, m = map(int,input().split())

#n개의점을 저장 받는다.
points = [] #가장 가까운 값 (min_heap)

for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(points, [(abs(x)+abs(y)),x, y])

#원점에서 가장 가까운 점을 하나 골라 해당 점의 x,y값을 2씩 더해주는 작업
for _ in range(m):
    point = heapq.heappop(points)

    point[1] = point[1]+2
    point[2] = point[2]+2

    heapq.heappush(points,[(abs(point[1])+abs(point[2])), point[1], point[2]])

answer = heapq.heappop(points)
print(answer[1],answer[2])