class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
	    
        i, j, found = 0, -1, False   
        for i, curr_interval in enumerate(intervals):
            print(curr_interval[0], curr_interval[1])
            
            # 범위 겹치지 않은 경우, newinterval이 현재값보다 큰 경우
            if curr_interval[1] < newInterval[0]:
                j = i
                
            # 범위 겹치지 않은 경우, newinterval이 현재값보다 작은 경우
            elif curr_interval[0] > newInterval[1]: 
                found = True; 
                break
		    
            # 범위 겹치는 경우 interval 업데이트 
            else: 
                newInterval = [min(newInterval[0], curr_interval[0]), max(newInterval[1], curr_interval[1])]
	    
        
        return intervals[:j+1] + [newInterval] + (intervals[i:] if found else [])
