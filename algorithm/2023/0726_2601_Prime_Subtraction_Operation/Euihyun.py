# 솔루션봄, 풀이 안해주셔 됩니다.
class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 에라토스테네스의 체 알고리즘을 사용하여 1000 이하의 소수를 구하기
        prime = [True] * 1001
        prime[0] = prime[1] = False
        for x in range(2, 1001):
            if prime[x]:
                # x의 배수들을 소수에서 제외
                for i in range(x * x, 1001, x):
                    prime[i] = False

        prev = 0  # 이전에 선택한 숫자의 값
        for x in nums:
            if prev >= x:
                return False  # 이전에 선택한 숫자보다 크거나 같은 숫자가 나오면 False를 반환

            # 현재 숫자 x에 대하여, 이전에 선택한 숫자와의 차이로 만들 수 있는 가장 큰 소수를 구함
            for p in range(x - 1, -1, -1):
                if prime[p] and x - p > prev:
                    break  # 가장 큰 소수를 찾았으므로 반복을 종료

            prev = x - p  # 차이를 prev에 저장하여 다음 숫자와 비교

        return True
