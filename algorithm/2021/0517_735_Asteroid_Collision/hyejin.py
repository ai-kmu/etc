class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            if ast < 0: # 역방향일 경우
                while stack and stack[-1] > 0 and stack[-1] < abs(ast): # 같은 방향으로 되거나 stack안에 있는 것보다 작을 때까지 반복
                    stack.pop(-1)
                    
                if stack and stack[-1] > 0: # 마지막 원소와 비교해서 pop하거나 하지 않음.
                    if stack[-1] == abs(ast):
                        stack.pop(-1)
                    continue
                        
            stack.append(ast) # stack의 마지막 원소가 negative이거나 ast가 positive일 때 append
            
        return stack
