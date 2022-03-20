class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        
        #left,right는 함수 안에서 앞으로 만들어야하는 '(' ')'의 수를 나타낸다
        #comb는 재귀함수에 들어가면서 만들어지는 "("와 ")"의 조합
        #left>0인 경우 left를 1 줄이면서 "("를 생성하고 늘어난 "("수에 맞춰 right에 1을 더함
        #right>0인 경우 ")"를 생성하고 right에 1을 뺌
        #left,right 모두 0인 경우 더이상 만들어야 할 괄호가 없으므로 리스트에 만들었던 조합을 append 해주고 return
        def recursion(left, right, comb):
            if(left == 0 and right == 0):
                answer.append(comb)
                return
            
            if(left > 0):
                recursion(left-1, right+1, comb+"(")
            
            if(right > 0):
                recursion(left, right-1, comb+")")
                
        recursion(n,0,"")
        
        return answer
    
'''
n = 2인 경우 (left,right)
"(" (1,1)
"((" (0,2) -> 더이상 left>0의 재귀함수에 들어갈 수 없고 right>0으로 넘어감
"(()" (0,1) -> left가 0이므로 right의 재귀문에 다시 들어감
"(())" (0,0) -> left,right 모두 0이므로 리스트에 추가하고 return

아까 "(("에서 right로 넘어가고 끝났기 때문에 함수를 나와서 "(" (1,1)의 right 조건문으로 들어감(left는 이미 들어갔다 나왔기 때문)

"()" (1,0) -> left가 1이기 때문에 left조건문으로 들어감
"()(" (0,1) -> left=0,right=1이기 때문에 right조건문으로 들어감
"()()" (0,0) -> left,right=0이므로 리스트에 추가하고 리턴하면 모든 함수에서 탈출

최종 출력 ["(())","()()"]

3부터는 너무 복잡해서 설명을 생략하도록 하겠습니다ㅠㅠ
'''
