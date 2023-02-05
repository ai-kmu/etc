import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 못풀겠어서 솔루션 참고했습니다.. 리뷰 안해줘도 돼요
        points = sorted([(l, -h, r) for l, r, h in buildings] + [(r, 0, None) for l, r, h in buildings])   
        answer = [[0, 0]]
        heap = [(0, float('inf'))]

        for x, neg_height, r in points:
            while x >= heap[0][1]:
                heapq.heappop(heap)
            if neg_height:
                heapq.heappush(heap, (neg_height, r))
            if answer[-1][1] != -heap[0][0]:
                answer.append([x, -heap[0][0]])
        return answer[1:] 
