# 정렬 후 앞에서부터 중복을 제거해나감

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals = sorted(intervals)
        answer = []
        for interval in intervals:
            is_add = True
            for i, answer_interval in enumerate(answer):
                if answer_interval[1] >= interval[0]:
                    answer[i][1] = max(answer[i][1], interval[1])
                    is_add = False
            if is_add:
                answer.append(interval)
        
        
        return answer
