class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        plus = []
        minus = []                          # 양수, 음수 따로 스택 쌓기
        for i in asteroids:                 # 처음부터 돌면서 경우의 수 확인
            sign = True if i>0 else False
            if sign:                        # 양수면 무조건 그냥 들어감
                plus.append(i)
            else:                           # 음수면 양수 리스트값 확인하면서 경우의 수 확인
                big = True
                while len(plus)>0:
                    if plus[-1]>abs(i):
                        big = False
                        break
                    elif plus[-1]==abs(i):
                        big = False
                        plus.pop()
                        break
                    else:
                        big = True
                        plus.pop()
                if big:
                    minus.append(i)
        return minus+plus
