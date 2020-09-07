class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals_len = len(intervals)
        
        # intervals length check
        if intervals_len == 0 or intervals_len == 1:
            return intervals
        
        # element[0]번째 오름차순 정렬
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # 새로운 intervals 초기화
        new_intervals = [intervals[0]]
        
        # 연속되는 element가 overlab되는지 check
        first_inter = intervals[0]
        for i in range(1, intervals_len):
            second_inter = intervals[i]
            
            # overlab될 경우 merge해줌.
            if first_inter[1] >= second_inter[0]:
                new_inter = [min(first_inter[0], second_inter[0]), max(first_inter[1],second_inter[1])]
                new_intervals[-1] = new_inter
            else:  
                new_intervals.append(second_inter)
                
            # new_intervals의 마지막 element을 first_inter로 사용
            first_inter = new_intervals[-1]
            
        return new_intervals
