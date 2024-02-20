# 처음 시도
# O(n^2)으로는 time limit(47/54)

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if len(values) == 2:
            return values[1] + values[0] - 1
        answer = 0
        for i, v in enumerate(values):
            for j in range(i+1, len(values)):
                answer = max(answer, i - j + v + values[j])
        return answer

# 답안 보고 공부함 리뷰 x
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        answer = cur = 0
        # O(n)으로 해결해야 함
        for v in values:
            # best score는 해당 인덱스의 값(서 있는 위치)과 지금 순회하는 값(볼 위치)의 합과 
            # 지금까지의 best score 값과 비교하면서 갱신할 수 있음
            answer = max(answer, cur + v)
            # cur : 바라볼 위치에 대한 변수
            # for문을 순회할 때마다 볼 위치의 거리가 1씩 멀어지므로 1씩 빼줌
            # 해당 인덱스의 값(서 있는 위치)이 현재 인덱스의 값(볼 위치)보다 작아지면 현재 인덱스의 값으로 대체(볼 위치로 이동함)
            cur = max(cur, v) - 1
        return answer
