import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:        
        courses.sort(key=lambda k: k[1])  # course를 데드라인 d를 기준으로 sorting
        start = 0
        que = []
        for t,d in courses:
            start += t
            heapq.heappush(que,-t)  # 젤 오래걸리는 course가 제일 윗쪽으로 갈수 있도록 heap구성
            while start > d: # 시작 day가 d를 이미넘어선 경우, que에서 가장 오래걸리는 course를 먼저 제거
                start += heapq.heappop(que)
        return len(que)
