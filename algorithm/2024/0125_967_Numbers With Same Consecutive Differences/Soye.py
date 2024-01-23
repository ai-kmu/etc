class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans=[]  # 정답 값을 저장

        def rec(x, tmp, ans):
            if x == n:  # tmp값의 자릿수가 n이 되면
                ans.append(tmp)
                return

            tmpp = tmp%10

            if tmpp-k >= 0:  # 차이 값이 0이상 이면
                store = tmp
                tmp = store*10 + tmpp-k
                rec(x+1, tmp, ans)
                tmp = store

            if k == 0:  # k값이 0일 때 중복을 방지하기 위해 ex) 11,11,22,22 -> 11,22로 중복 제거
                return

            if tmpp+k <= 9:  # 차이 값이 0이하 이면
                store = tmp
                tmp = store*10 + tmpp+k
                rec(x+1, tmp, ans)
                tmp = store
        
        for i in range(1, 10):
            rec(1, i, ans)

        return ans
