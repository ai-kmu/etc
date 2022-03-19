class Solution(object):
    def generateParenthesis(self, n):
        
        # 가운대에 )) , (( , )( , () 을 추가시키는 방식
        
        # [모양,왼쪽 '(' 개수, 오른쪽 ")" 개수]
        
        answers = [["()",0,0]]
        
        for i in range(1,n):
            
            temp_answer = []
            
            for answer in answers:
                
                # 가운대 )) , (( , )( , () 를 넣었을때, 완전한 모양을 만들 수 있으면 (pair가 없이 바깥을 향하는것이 안되도록) 
                # 마지막이 아니거나 마지막 괄호를 넣을때 완전한 모양이 되면 '(' 의 개수와 ')' 의 개수가 동일 하면
                
                if (answer[1] + 1 <= (i+1)//2 and answer[2] <= (i+1)//2) and (i+1 != n or (answer[1] + 1) + (n - answer[2]) == n): 
                    temp_answer.append([answer[0][:i] + "))" + answer[0][-i:], answer[1] + 1, answer[2]])
                        
                if (answer[1] <= (i+1)//2 and answer[2] + 1 <= (i+1)//2) and (i+1 != n or answer[1] + n - (answer[2] + 1) == n):
                    temp_answer.append([answer[0][:i] + "((" + answer[0][-i:], answer[1], answer[2] + 1])
                        
                if (answer[1] + 1 <= (i+1)//2 and answer[2] + 1 <= (i+1)//2) and (i+1 != n or (answer[1] + 1) + n - (answer[2] + 1) == n):
                    temp_answer.append([answer[0][:i] + ")(" + answer[0][-i:], answer[1] + 1, answer[2] + 1])
                
                if i+1 != n or answer[1] + n - answer[2] == n:
                    temp_answer.append([answer[0][:i] + "()" + answer[0][-i:], answer[1], answer[2]])
    
            answers = temp_answer
        
        final_answer = []
        for j in range(len(answers)):
            final_answer.append(answers[j][0])
            
        return final_answer
