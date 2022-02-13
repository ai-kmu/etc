class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 2개의 바구니
        # 각 바구니는 한 종류의 과일만, 개수는 많을 수록 좋다.
        # 오른쪽으로 이동
        # 두 바구니에 없는 과일을 만나면, 한 과일을 버리고 새거를 담거나 멈추거나
        # 두 바구니 과일 합이 최대가 되는 경우는?
        
        count = 0
        
        
        for i in range(len(fruits)):
            
            for f in fruits:
                if f in stack:
                    count += 1
                    stack.append(f)
                    continue
                    
        return count + 1
