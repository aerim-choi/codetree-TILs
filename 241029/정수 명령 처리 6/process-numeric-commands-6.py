import heapq

class priortyQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -heapq.heappop(self.items)

    def top(self):
        if self.empty():
            raise Exception("PriortyQueue is empty")

        return -self.itmes[0]


n = int(input())
priorty_queue = priortyQueue()
for _ in range(n):
    
    command = input().split()

    if command[0]=="push":
        priorty_queue.push(int(command[1]))
    elif command[0]=="pop":
        value = priorty_queue.pop()
        print(value)
    elif command[0]=="size":
        print(priorty_queue.size())
    elif command[0]=="empty":
        if priorty_queue.empty():
            print(1)
        else:
            print(0)
    else:
        print(priorty_queue.top())