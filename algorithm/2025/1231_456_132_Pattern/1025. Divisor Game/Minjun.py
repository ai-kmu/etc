class Solution:
    def divisorGame(self, n: int) -> bool:
        # x는 자기자신 제외한 n의 약수 
        # 1을 남기면 이김
        # 홀수면 짐.
        if n % 2 != 0:
            return False
        return True
