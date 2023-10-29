# 못풀고 참고했습니다. 리뷰 안해주셔도 됩니다.
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        are_values_same = True  # 값이 같은지 여부를 나타내는 플래그

        # n번째 행의 총 요소 수를 계산 
        n = 2**(n - 1)

        # 첫 번째 행에 도달할 때까지 반복
        while n != 1:
            # 행의 요소 수를 반으로 나눔
            n //= 2

            # 만약 k가 행의 두 번째 절반에 속한다면 k를 조정하고 플래그 토글
            if k > n:
                k -= n
                are_values_same = not are_values_same

        # 플래그가 값이 같음을 나타내면 0을 반환, 그렇지 않으면 1을 반환
        return 0 if are_values_same else 1
