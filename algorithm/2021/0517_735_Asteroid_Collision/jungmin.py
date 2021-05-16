class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = [] # 최종 결과 출력할 리스트 생성
        for ast in asteroids: # asteroid 원소마다
            # result 마지막 원소가 양수이고 현재 asteroid 원소가 음수일 때
            # (result 마지막 원소가 음수이고 현재 asteroid가 양수이면 서로 만나지 않으므로 while문 안으로 가지 말아야함.)
            while result and result[-1] > 0 and ast < 0:
                if result[-1] + ast < 0: result.pop() # 서로 더한 결과가 음수이면 result 마지막 원소 제거
                elif result[-1] + ast > 0: break   # 서로 더한 결과가 양수이면 break하고 다음 asteroid 원소 for문 진입
                else: result.pop(); break  # 서로 더한 결과가 0이면 result 마지막 원소 제거하고 break하고 다음 asteroid 원소 for문 진입
            else: result.append(ast) # 현재 asteriod 원소를 result에 저장        
        return result
