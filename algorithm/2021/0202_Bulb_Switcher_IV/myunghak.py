# 그냥 바뀔때 마다 1씩 더해주면 됨
# 단 1로 시작하면 위 값에서 1을 더해주어야 함


class Solution:
    def minFlips(self, target: str) -> int:
        return sum([target[i]!=target[i+1]  for i in range(len(target)-1)])+ (target[0] =="1")
