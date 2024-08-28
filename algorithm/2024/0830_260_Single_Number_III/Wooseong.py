from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        cnt = 0
        answer = []
        # 이거 쓰면 iterable를 가지고 {요소: 개수} 형태의 `Counter` 객체로 만듦
        for k, v in Counter(nums).items():
            # 한 개인 걸 answer에 넣기
            if v == 1:
                answer.append(k)
                cnt += 1
            # 좀 더 빠르게 종료하기 위해 1개짜리 두 개되면 바로 종료
            if cnt == 2:
                return answer
