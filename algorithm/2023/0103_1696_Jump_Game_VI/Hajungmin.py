from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        # (score, index)로 dq에 넣어줌
        dq = deque([(nums[0],0)])

        # 1번부터 돌면서 dq에 있는 score와 다음 단계로 갔을 때 계산되는 score를 비교
        for i in range(1, len(nums)):
            score = dq[0][0] + nums[i]
            
            # dq에 있는 score가 계산된 score보다 작을 때 
            # 현재 score보다 커질 때까지 pop을 한다
            while dq and dq[-1][0] < score: 
                dq.pop()
            
            # 계산된 score를 인덱스와 함께 dq에 넣어준다
            dq.append((score,i))
            
            # 한번에 k만큼 점프할 수 있기 때문에 만약 현재 인덱스에서 k를 뺀 것이 
            # dq의 0번째 요소의 인덱스와 같게 되면 dq의 0번째 요소를 없앤다
            # 이런 식으로 범위를 한정해가며 점프를 할 수 있는 모든 경우의 수들을 비교한다
            if dq[0][1] == i - k: 
                dq.popleft()
        
        return dq[-1][0]
