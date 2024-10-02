# fail code
# 리뷰 x

class Solution:
    def minFlips(self, s: str) -> int:

        s_1 = s
        s_2 = s[1:]+s[0]

        answer_1 = 0 # 짝수번째를 1로, 홀수번째는 0으로
        answer_2 = 0 # 홀수번째를 1로, 짝수번째는 0으로
        for i, s_i in enumerate(s_1):

            # 짝수번째
            if i % 2 == 0:
                if s_i == "1":
                    answer_2 += 1 
                else:
                    answer_1 += 1 
            # 홀수번째
            else:
                if s_i == "1":
                    answer_1 += 1 
                else:
                    answer_2 += 1 
     
        return min(answer_1,answer_2)
                
