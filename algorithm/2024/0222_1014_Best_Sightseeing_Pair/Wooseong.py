'''
score = values[i] + values[j] + i - j
인데 이걸 다르게 표현하면
score = (values[i] + i) + (values[j] - j) = rewarded + penalted
가 된다. 이때 i < j이므로
정답은 특정 시점의 최대 rewarded (max_rewarded)에
가능한 penalted를 더한 것 중 최대가 된다
'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        answer = 0
        max_rewarded = values[0]  # + 0 생략
        for i in range(1, len(values)):
            # max_rewarded에 penalted를 더한 것과 answer 비교
            answer = max(answer, max_rewarded + values[i] - i)
            # max_rewarded 갱신
            max_rewarded = max(max_rewarded, values[i] + i)
        
        return answer
