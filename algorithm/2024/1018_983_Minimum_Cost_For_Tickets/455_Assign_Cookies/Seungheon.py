class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # greedy하게 작은것부터 부여
        # s 쿠키
        # g 사람

        answer = 0
        s.sort()
        g.sort()

        c_idx = 0
        for i, s_i in enumerate(s):
            if c_idx >= len(g):
                return answer

            if s_i >= g[c_idx]:
                answer += 1
                c_idx += 1


        return answer
