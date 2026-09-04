class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # numRows = 1이면 필요없음
        if numRows <= 1:
            return s

        s_list = ["" for _ in range(numRows)]
        i, j, c = 0, 0, -1

        # zigzag -> 결국 idex 증감하면서 각 numRows에 문자 쌓기
        for i in range(len(s)):
            if j == 0 or j == numRows - 1:
                c *= -1
            
            s_list[j] += s[i]
            j += c
            
        return "".join(s_list)
