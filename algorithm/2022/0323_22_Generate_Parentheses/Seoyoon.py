"""
오른쪽 괄호 수가 왼쪽 괄호 수 보다 많으면 조건이 만족되지 못한다. .
왜냐면 오른쪽 괄호는 이전 왼쪽 괄호랑 짝을 맞춰야하는데
이렇게되면 나중에 왼쪽 괄호 몇개를 추가해도 오른쪽 괄호와 일치하지 않게 될 수 있다.
그래서 )개수가 (개수를 넘지 않도록 재귀하며 증가시키면 된다. 
"""


class Solution(object):
    def generateParenthesis(n):
        # 결과 담을 리스트
        ans = []
        #s: string 전체 괄호 수, left: '(' 즉 왼쪽 괄호, right: ')'오른쪽 괄호
        def recursion(s = '', left = 0, right = 0):
            if len(s) == 2 * n: # 전체 개수되면 append한다.
                ans.append(s)
                return
            
             # left (개수가 전체 괄호쌍 수보다 작으면 (추가
            if left < n:
                recursion(s+'(', left+1, right)
                
            # right ) 개수가 왼쪽괄호 (보다 작으면 )추가
            if right < left: 
                recursion(s+')', left, right+1)
            # 바로 left후에 right가 붙으니까 (다음에 )가 차례로 잘 올 수 있다.
        recursion()
        return ans
    
"""
    (-> (( -> ((( -> ((())) 
       -> (() -> (()( -> (()() -> (()())
              -> (()) -> (())( -> (())()
       
 -> () -> ()( -> ()(( -> ()(() -> ()(())
              -> ()() -> ()()( -> ()()()

시간복잡도는 O(2^2n)
recursion 함수 두번 호출하면서 최종 문자가 나올때까지 계속 도니까 2^2n
2n인 이유는 길이가 2n이 될 때 재귀함수가 종료되니까"""
