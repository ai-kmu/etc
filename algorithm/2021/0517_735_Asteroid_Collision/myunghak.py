class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = [asteroids[0]]
        for i in range(1, len(asteroids)):
            dst = False # 현재 소행성이 파괴되었는지 기록
            while(len(ans) > 0 and ans[-1] >0 and asteroids[i] < 0):
                if(ans[-1]<-asteroids[i]):
                    ans.pop() # ans에 있는 소행성 파괴, 현재 소행성 파괴되지 않고 계속 진행
                else:
                    if(ans[-1]==-asteroids[i]):
                        ans.pop()
                    dst=True # 파괴됨
                    break
            if not dst:
                ans.append(asteroids[i])
        return ans
