class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        li = []
        
        intervals.sort(key=lambda x: x[0])  #리스트 정렬
        
        if intervals:
            li = [intervals[0]]
        
        for interval in intervals[1:]:
            if li[-1][1] >= interval[0]:  #이전 리스트의 오른쪽값과 현재 리스트
                li[-1][1] = max(li[-1][1],interval[1])
                li[-1][0] = min(li[-1][0],interval[0])
                
            else:
                li.append(interval)
                
        return li
