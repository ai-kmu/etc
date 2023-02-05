# 풀이 실패
# 다른 사람 풀이 참고해서 
import heapq 
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        answer = [(0, 0)]
        lines = []
        heap = [(0, 10**4)]
        # 왼쪽 꼭짓점과 오른쪽 꼭짓점을 구분해서 lines에 추가
        # 1번째 : 왼쪽 꼭짓점의 위치, 높이, 왼쪽인지 오른쪽인지 구분하는 flag
        # 2번째 : 오른쪽 꼭짓점의 위치
        for l, r, h in buildings:
            lines.append((l, -h, r))
            lines.append((r, 0, 0))
        # x축의 위치에 따라서 sort
        lines.sort()
        for x, h, r in lines:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if h:
                heapq.heappush(heap, (h, r))
            if answer[-1][1] != -heap[0][0]:
                answer.append((x, -heap[0][0]))
        return answer[1:]
