# 16. 프로그래머스 - 무지의 먹방 라이브

# 이진 트리기반 최소 힙 자료구조 사용, 우선순위 큐
import heapq as hq

def solution(food_times, k):
    # 음식 순서값 저장
    answer = 0

    # food_times redefine(food, food`s position)
    food_times = [(food, pos) for pos, food in enumerate(food_times, 1)]
    # print('Redefine food_times : ', food_times)
    hq.heapify(food_times)
    # print('Insert food_times to minHeap : ', food_times)

    # smallest size of food
    smallest_food = food_times[0][0]
    prev_food = 0
    # 작은 음식 완전히 소비, 원판 완주
    while k - ((smallest_food - prev_food) * len(food_times)) >= 0:
        # 해당 음식 끝나는 시간만큼 뺀다
        k -= (smallest_food - prev_food) * len(food_times)
        prev_food, position = hq.heappop(food_times)
        if not food_times:
            answer = -1
            return answer
        smallest_food = food_times[0][0]
    food_times = sorted(food_times, key=lambda x : x[1])
    answer = food_times[k % len(food_times)][1]
    return answer

food_time_1 = [3, 1, 2]
k_1 = 5
print(solution(food_time_1, k_1))

# class CircularQueue():
#     def __init__(self, max=2000):
#         self.max = max
#         self.queue = [None] * self.max
#         self.size = self.front = 0
#         self.rear = None
#
#     def is_empty(self):
#         return self.size == 0
#
#     def is_full(self):
#         if self.rear == None:
#             return False
#         return self.next_index(self.rear) == self.front
#
#     def next_index(self, idx):
#         return (idx + 1) % self.max
#
#     def enqueue(self, data):
#         if self.is_full():
#             raise Exception('Queue is Full')
#
#         if self.rear == None:
#             self.rear = 0
#         else:
#             self.rear = self.next_index(self.rear)
#
#         self.queue[self.rear] = data
#         self.size += 1
#         return self.queue[self.rear]
#
#     def deque(self):
#         if self.is_empty():
#             raise Exception('Queue is empty')
#         self.queue[self.front] = None
#         self.front = self.next_index(self.front)
#         return self.queue[self.front]
#
#     def display(self):
#         print(self.queue)

