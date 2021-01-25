# DNA 배열을 4진법으로 생각하고 풀기

class Solution:
    def findRepeatedDnaSequences(self, s):
        def n2l(L): # 4진법을 10진법으로
            l_dict = {0: "A", 1 : "C", 2 :"G", 3: "T"}
            r = ""
            for i in range(10):
                r+= l_dict[L%4]
                L = L>>2
            return r
        
        f_p_t = 4**9 # 미리 계산해놓는게 빠를것 같아서....
        l2n = {"A": 0, "C" : 1, "G" :2, "T": 3} # 4진법에서 10진법으로 바꾸기 위한 dict
        N = sum([(4**i) * l2n[l] for i, l in enumerate(s[:10])]) # 4진법을 10진법으로
        my_set = set([N]) # 나온 것들 저장할곳
        answer = set([])  # 정답 저장할 곳
        for i in range(10, len(s)):
            N = (N >> 2) + l2n[s[i]] * f_p_t # 비트상으로 2칸 밀고 새로운 문제어 4^9을 곱해 더해주면 4진법상 다음 문자에 해당하는 숫자가 나옴
            if N in my_set:
                answer.add(N)
            else:
                my_set.add(N)
        return [n2l(C) for C in answer] # 4진법을 10진법으로 바꿔서 return
