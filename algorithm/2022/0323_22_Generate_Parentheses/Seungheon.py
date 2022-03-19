class Solution(object):
    def generateParenthesis(self, n):
        
        # 가운데 )) , (( , )( , () 를 추가하는 방식
        
        # [모양,왼쪽 '(' 개수, 오른쪽 ")" 개수]
        
        answers = [["()",0,0]]
        
        for i in range(1,n):
            
            temp_answer = []
            
            for answer in answers:
                
                # 가운데 )) , (( , )( , () 를 넣었을때, 완전한 모양을 만들 수 있으면 (pair가 없이 바깥을 향하는것이 안되도록) 
                # 마지막이 아니거나 마지막 괄호를 넣을때 완전한 모양이 되면 '(' 의 개수와 ')' 의 개수가 동일 하면
                
                for left, right, shape in zip([1, 0, 1, 0],[0, 1, 1, 0],["))", "((", ")(", "()"]):
                    if (answer[1]+left <= (i+1)//2 and answer[2]+right <= (i+1)//2) and (i+1 != n or (answer[1]+left) + n-(answer[2]+right) == n):
                        # 마지막 추가시에는 shape만 answers에 저장
                        if len(answer[0])+2 == 2*n:
                            temp_answer.append(answer[0][:i]+shape+answer[0][-i:])
                        else: 
                            temp_answer.append([answer[0][:i]+shape+answer[0][-i:], answer[1]+left, answer[2]+right])
    
            answers = temp_answer
        if n == 1:
            answers = ["()"]
        return answers
