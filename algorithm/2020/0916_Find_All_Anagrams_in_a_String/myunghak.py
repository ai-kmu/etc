# 현재 찾아야할 문자를 check 변수에 넣고
# 이미 찾은 문자를 bucket 변수에 넣은 후
# bucket에 찾아야 할 모든 문자가 들어가면 answer에 그 index를 append해줌


class Solution:
    def Solution():
        bucket = ""
        check = ""
    def input_ch(self,n):
        self.bucket += self.check[n]
        self.check = str(self.check[:n] + self.check[n+1:])
    def output_ch(self):
        self.check+=self.bucket[0]
        self.bucket = self.bucket[1:]
    
    def findAnagrams(self, s,p):
        answer = []
        len_p = len(p)
        self.check = str(p)
        self.bucket = ""
        for i, ch in enumerate(s):
            n = self.check.find(ch)
            if n>= 0:
                self.input_ch(n)
            if n == -1:
                n = p.find(ch)
                if n < 0:
                    self.bucket = ""
                    self.check = str(p)
                else:
                    while(ch not in self.check):
                        self.output_ch()
                    n = self.check.find(ch)
                    if n>= 0:
                        self.input_ch(n)
            if len(self.check) == 0:
                answer.append(i-len_p+1)
                self.output_ch()
                
                
        return answer
A = Solution()
    
A.findAnagrams("abacbabc", "abc")
