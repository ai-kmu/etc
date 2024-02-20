# i와 j를 분리해서 식 정리
# i의 max값이 따로 저장되어야 함 
class Solution:
    def maxScoreSightseeingPair(self, values): 
        max_i = 0 
        max_score = 0
        for i in range(1, len(values)):
            # 계산된 값보다 큰지 작은지 판단
            max_i = max(max_i, values[i-1]+i-1)
            max_score = max(max_score, max_i+values[i]-i)
        return max_score
