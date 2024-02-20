# DP : O(n)으로 풀이
class Solution:
    def maxScoreSightseeingPair(self, values):
        max_score = 0
        max_prev = values[0]

        for j in range(1, len(values)):
            # 최대 점수 갱신
            # 기존의 최댓값과 이전의 최댓값에 현재 경우를 더한 것과 비교
            max_score = max(max_score, max_prev + values[j] - j)
            # 이전까지의 최대값 갱신
            max_prev = max(max_prev, values[j] + j)
            
        return max_score
