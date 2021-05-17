class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for id in asteroids:
          
            # 양수는 왼쪽-> 오른쪽을 의미하고, 음수는 오른쪽-> 왼쪽을 의미
            # 충돌은 현재 astero right-> left 및 마지막 astero가 left-> right 일 때만 발생
            
            # 마지막 값이 양수이고 현재 값이 음수일때 
            if not stack or stack[-1]*id>0 or stack[-1]<0:
                stack.append(id)
            elif abs(id)>=abs(stack[-1]):
                while stack and stack[-1]>0 and abs(id) > abs(stack[-1]):
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(id)
                elif stack[-1] == -id:
                    stack.pop()
        return stack
        
