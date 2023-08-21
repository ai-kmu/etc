class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        char = ['a', 'b', 'c']
        ans = []
        # 길이 n까지 직전 문자와 겹치지 않게 string 생성
        def making(st):    
            for c in char:
                if st[-1] == c:
                    continue
                if len(st) == n:
                    ans.append(st)
                    return
                making(st+c)
        for c in char:
            making(c)
        # trivial case
        if len(ans) < k:
            return ""

        return ans[k-1]
