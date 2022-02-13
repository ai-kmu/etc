class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window 문제
        
        l = 0 # 왼쪽 인덱스
        ans = 1 # 정답값
        basket = {} # 과일 담는 basket. 2개 type만 들어가야 한다.
        
        # friut를 오른쪽 인덱스를 이용하여 순차적으로 이동
        # 현재 과일 r_key를 basket에 넣어서 갯수 센다.
        # basket 안에 2개 이상의 type이 들어가 있으면
        # 2개가 될 때 까지 왼쪽 인덱스를 하나씩 증가시키면서
        # 왼쪽 인덱스가 가리키는 과일 type의 갯수를 basket에서 하나씩 감소시킨다.
        # 그리하여 해당 과일이 한개 남으면 basket에서 제거
        # basket에 2개 type만 남을 때 ans로 가장 긴 window를 구한다.
        for r, r_key in enumerate(fruits):
            basket[r_key] = basket.get(r_key, 0) + 1
            while len(basket) > 2:
                l_key = fruits[l]
                if basket[l_key] == 1:
                    del basket[l_key]
                else:
                    basket[l_key] = basket[l_key] - 1
                l = l + 1
            ans = max(ans, r - l + 1)
        
        return ans
