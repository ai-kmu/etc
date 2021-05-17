class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        # 하나씩 포함
        for asteroid in asteroids:
            stack.append(asteroid)
            
            # 서로 충돌하게 되면서 길이가 2가 넘으면
            while len(stack) >= 2 and (stack[-2] > 0 and stack[-1] < 0):
                
                # 충돌하는 두개를 가져와서 
                last1 = stack.pop()
                last2 = stack.pop()
                # 두개중 충돌했을 때 큰것만 남겨둠
                if abs(last1) > abs(last2):
                    stack.append(last1)
                elif abs(last2) > abs(last1):
                    stack.append(last2)
        return stack
