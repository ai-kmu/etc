# n = m에 대한 답은
# m - 1 = a + b를 만족하는 음이 아닌 정수 a,b에 대하여
# ({a의원소}){b의원소} 이다
# a의 원소 앞 뒤로 ()를 쳐주어, a와 b의 괄호 수를 합치면 m-1이 되어야 한다.

class Solution:
    # 0 ~ n까지 모든 값에 대한 답을 저장할 dictionary 지정
    def __init__(self):
        self.all_ans = {0:[''], 1:['()']}

    
    # m에 대한 답을 return하는 함수
    def generateSub(self, m):
        temp = []
        for i in range(m):                      # m-1 =
            for x in range(len(self.ans[i])):   #       a + 
                for y in range(len(self.ans[m-1-i])): #     b(=m-1-a)
                    cand = '({}){}'.format(self.all_ans[i][x], self.all_ans[m-1-i][y])
                    if cand not in temp: temp.append(cand)

        return temp

    def generateParenthesis(self, n):
        # 2부터 n까지 하나씩 dictionary update
        for m in range(2,n+1):
            self.all_ans[m] = self.generateSub(m)

        return self.all_ans[n]

## Run code : 40, 58, 62ms
## Submit (ms, MB) - (40, 14.3), (48, 14.2), (60, 14.3)
