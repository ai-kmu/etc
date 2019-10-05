## 1
def solution(operations):
    queue = []
    for i in operations:
        op, num = i.split()
        if op == "I":
            queue.append(int(num))
        elif op == "D" and queue:
            if num == "-1":
                queue.remove(min(queue))
            elif num == "1":           
                queue.remove(max(queue))

    if queue:
        return [max(queue), min(queue)]
    else:
        return [0,0]
    
    
    
    

## 2
import heapq

def solution(operations):
    queue = []
    
    for i in operations:
        op, num = i.split()
        if op == "I":
            heapq.heappush(queue ,int(num))
        elif op == "D" and queue:
            if num == "-1":
                 heapq.heappop(queue)
            elif num == "1":
                queue.pop(queue.index(max(queue)))               

    if queue:
        return [max(queue), heapq.heappop(queue)]
    else:
        return [0,0]
