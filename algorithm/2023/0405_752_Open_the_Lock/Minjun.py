# 풀이 실패 쒸익쒸익
# 다시 풀다가 만 코드여서 리뷰 안 해도 됩이다

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # a = int(target)
        # b = [a-1,a+1,a-10,a+10,a-100,a+100,a-1000,a+1000]
        a,b,c,d = target
        nums = [int(a),int(b),int(c),int(d)]
        ans = 0
        def counter(n):
            for i in nums:
                ans += min(abs(10-i), i)
        tmp = ""
        for i, n in enumerate(nums):
            while n != 0:
                if n > 5:
                    n = (str(n+1))
                tmp = target[:i] + n + target[i+1:]
                if tmp in deadends:
                    break


                else:
                    n-1
