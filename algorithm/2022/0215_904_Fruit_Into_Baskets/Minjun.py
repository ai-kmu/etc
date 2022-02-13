class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 2개의 바구니
        # 각 바구니는 한 종류의 과일만, 개수는 많을 수록 좋다.
        # 오른쪽으로 이동
        # 두 바구니에 없는 과일을 만나면, 더 먼저 담았던 과일을 버리고 새거를 담거나 멈추거나
        # 두 바구니 과일 합이 최대가 되는 경우는?
        
        # pointer 이용, 과일 종류 3가지 판단 후 삭제
        # 3가지 종류가 되기 전까지 계속 pointer 증가.
        # 3가지 종류가 되면, 지금의 길이를 기록하고 먼저 담긴 걸 제외.
        
        
        basket = {}  # 과일 바구니
        l_point = 0  # 왼쪽 포인터
        answer = 1  # 최소 과일 수 1
        
        for r_point, r_key in enumerate(fruits):
            
            basket[r_key] = basket.get(r_key, 0) + 1
            while len(basket) > 2:
                l_key = fruits[l_point]
                if basket[l_key] == 1:
                    del basket[l_key]
                else:
                    basket[l_key] = basket[l_key] - 1
                l_point += 1
            answer = max(answer, r_point - l_point + 1)
        
        return answer
