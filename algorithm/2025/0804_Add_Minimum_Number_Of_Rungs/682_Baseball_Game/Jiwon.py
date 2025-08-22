class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tmp = []
        ans = 0

        for ops in operations:
            if ops not in ["+", "C", "D"]:
                tmp.append(int(ops))
                ans += tmp[-1]
            elif ops == "+":
                tmp.append(tmp[-1] + tmp[-2])
                ans += tmp[-1]
            elif ops == 'D':
                tmp.append(2 * tmp[-1])
                ans += tmp[-1]
            elif ops == "C":
                ans -= tmp.pop()
        return ans
