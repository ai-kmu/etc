class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        minmax_arr = []
        for interval in intervals:
            is_add = True
            for i, check in enumerate(minmax_arr):
                if check[0] <= interval[0] <= check[1] or check[0] <= interval[1] <= check[1] or interval[0]<check[0]<interval[1]:
                    minmax_arr[i][1] = max(interval[1], minmax_arr[i][1])
                    minmax_arr[i][0] = min(interval[0], minmax_arr[i][0])
                    is_add = False
                    break
                    
                    
            if is_add:
                minmax_arr.append(interval)
        
        minmax_arr = sorted(minmax_arr)
        answer = []
        for interval in minmax_arr:
            is_add = True
            for i, answer_interval in enumerate(answer):
                if answer_interval[1] >= interval[0]:
                    answer[i][1] = max(answer[i][1], interval[1])
                    is_add = False
            if is_add:
                answer.append(interval)
        
        
        return answer
