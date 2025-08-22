class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for idx in operations:
            if idx =='C':
                ans.pop()
            elif idx == 'D':
                ans.append(ans[-1]*2)
            elif idx == '+':
                tmp = ans[-1] + ans[-2]
                ans.append(tmp)
            else:
                ans.append(int(idx))

        return sum(ans)
        
