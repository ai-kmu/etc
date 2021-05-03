class Solution(object):
    def solve_overlap(self,arr, i): # 중복 제거
        if i > 0 and arr[i][0] <= arr[i-1][1]:            
            arr[i-1:i+1] = [[min(arr[i-1][0], arr[i][0]), max(arr[i][1], arr[i-1][1])]]
            return self.solve_overlap(arr, i-1)
        elif i+1 < len(arr) and arr[i][1] >= arr[i+1][0]:
            arr[i:i+2] = [[min(arr[i][0], arr[i+1][0]), max(arr[i][1], arr[i+1][1])]]
            return self.solve_overlap(arr, i)
        return arr

    def insert(self, intervals, newInterval):
        for i in range(len(intervals)):  # 중간에 new Interval을 삽입 후 중복 제거
            if intervals[i][0] <= newInterval[0] or intervals[i][0] <= newInterval[1]:
                j = i
                while(j < len(intervals) and intervals[j][0]<newInterval[1]):
                    j+=1
                intervals = intervals[:j] + [newInterval] + intervals[j:] 
                return self.solve_overlap(intervals, j)
                
        
        # 예외 처리
        if len(intervals) == 0:
            return [newInterval]
        elif newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        
