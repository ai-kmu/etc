#.... 봐버렸읍니다... 리뷰안해주셔도 돼요.....
class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def dfs(n, num):
            # 남은 자릿수가 0인 경우 현재 숫자를 반환
            if n == 0:
                return [num]
            result = []  
            # 현재 숫자의 일의 자리 숫자
            last_digit = num % 10  

            # 다음 숫자를 생성할 때 일의 자리 숫자에 k를 더한 숫자가 10 미만인 경우에 추가
            if last_digit + k < 10:
                result += dfs(n - 1, num * 10 + last_digit + k)

            # k가 0이 아니고, 일의 자리 숫자에서 k를 뺀 숫자가 0 이상인 경우에 추가
            if k != 0 and last_digit - k >= 0:
                result += dfs(n - 1, num * 10 + last_digit - k)

            return result

        # n이 1인 경우 0부터 9까지의 모든 숫자
        if n == 1:
            return list(range(10))

        result = []
        for i in range(1, 10):
            result += dfs(n - 1, i)

        return result


            
