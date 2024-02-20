class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        # max value를 i가 될 수 있는 최댓값으로 두기
        # j가 멀어질때마다 max_value의 값을 빼줌
        
        max_value = values[0] - 1
        max_value_idx = 0
        answer = 0

        for v in values[1:]:
            answer = max(answer, max_value + v)
            if max_value < v:
                max_value = v - 1
            else:
                max_value -= 1
            
        return answer
