from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # a + rev(b) == rev(a) + b 를 만족하는 (a, b)의 쌍을 찾는 문제
        # 이는 a - rev(a) == b - rev(b) 를 만족하는 쌍을 찾는 것과 동일하다.
        
        # 따라서 nums안의 모든 숫자들을 다음과 같이 변경한다.
        nums = [n - int(str(n)[::-1]) for n in nums]
        
        # 그리고 서로 동일한 쌍을 찾아야 하기 때문에 Counter를 활용해
        # 같은 값을 같는 case의 수를 찾는다.
        counter = Counter(nums)
        
        answer = 0
        for c in counter.values():
            # 만약 count한 수가 1보다 클 경우
            if c > 1:
                # C(n, 2)만큼 answer에 더해준다.
                answer += c * (c-1) // 2
        
        return answer % (10**9+7)
