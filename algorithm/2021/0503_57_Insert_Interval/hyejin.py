class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 새로운 범위 추가하고 정렬
        intervals.append(newInterval) 
        intervals.sort()
        
        
        answer = []
        
        # 범위 시작과 끝 초기화
        start = intervals[0][0]
        end = intervals[0][1]
        
        for first, second in intervals:
            # 만약 현재 범위 앞보다 end가 더 작다면 범위외이므로 start, end 업데이트하고, 다시 초기화
            if end < first:
                answer.append([start, end])
                start = first
                end = second

            # fisrt가 start보다 작을 경우, start = first
            if start > first:
                start = first
            # second가 end보다 크거나 같고, first도 end보다 크거나 같으면 end = second
            if second >= end and first <= end:
                end = second
    
        # 마지막 start, end update
        answer.append([start, end])
        return answer
