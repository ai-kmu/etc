from collections import deque

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right = deque()
        answer = []
        for ast in asteroids:                            
            if not right and ast < 0:                  # 왼쪽으로 가는 소행성인 경우, 오른쪽으로 가는 소행성이 없는 경우
                answer.append(ast)                     # 정답에 추가
            else:
                if ast > 0:                            # 오른쪽으로 가는 소행성인 경우
                    right.append(ast)                  # 리스트에 추가
                else:                                  # 왼쪽으로 가는 소행성의 경우
                    while right:                       # 오른쪽으로 가는 소행성이 있는 경우 
                        right_ast = right.pop()        
                        if abs(ast) < right_ast:       # 오른쪽으로 가는 소행성이 더 큰 경우
                            right.append(right_ast)    # 왼쪽으로 가는 소행성 파괴
                            break                 
                        elif abs(ast) == right_ast:    # 둘 크기가 같은 경우
                            break                      # 둘 다 파괴
                        else:                          # 왼쪽이 더 큰 경우
                            if not right:              # 오른쪽으로 가는 소행성이 없는 경우 
                                answer.append(ast)     # 정답에 왼쪽으로 가는 소행성 추가
        while right:                                   
            answer.append(right.popleft())             # 나머지 오른쪽으로 가는 소행성을 접답에 추가
        return answer
