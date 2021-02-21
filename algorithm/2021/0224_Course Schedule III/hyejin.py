from heapq import heappush, heappop
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        curr = 0 # 현재 날짜
        courses.sort(key=lambda x: x[1]) # 끝나는 순대로 정렬
        max_heap = [] #max heap 리스트
        
        for duration, end in courses:
            if curr+duration <= end: # 이 강의를 수강할 수 있다면 듣기
                curr += duration
                heappush(max_heap, -duration)
            elif max_heap and duration < -max_heap[0]:
                """
                아니라면 이 강의나 이전에 넣었던 강의 중 하나는 무조건 못듣는 것이기 때문에 선택을 해야함
                선택할 때, 이전강의보다 이번 강의의 duration이 더 작다면 다음 강의를 들을 수 있는 시간이 늘어남
                즉 현재 duration과 이전 강의의 max 값을 비교하여 더 큰 것을 빼면 됌.
                """
                curr -= -heappop(max_heap)
                curr += duration
                heappush(max_heap, -duration)
                
        return len(max_heap)
