class Solution:
    
    """
    보니까 Output이 반드시 정렬되어 있어야하는 건 아님
    따라서 각 Element가 어떻게 생성되는 지만 파악하고 만들어서 리턴해주면 됨.
    
    
    """
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 1:
            return ["()"]
        
        ans = set()
        
        for i in self.generateParenthesis(n-1):
            for j in range(len(i)):
                ans.add(i[0:j+1]+"()"+i[j+1:len(i)])
                print("i : ",i," | len(i) : ",len(i), " | j : ", j," | ans", ans)
        ans = list(ans)

        return ans

"""
각 for loop이 돌아가는 상태를 보면,


i :  ()  | len(i) :  2  | j :  0  | ans {'(())'}

i[0:1]+"()"+i[1:2] 을 ans 에 추가해줌으로써,
( + ( + ) + ) 이것이 ans 에 들어간다.
따라서 ans는 "(())"이 생긴다.

i :  ()  | len(i) :  2  | j :  1  | ans {'()()', '(())'}

i[0:2]+"()"+i[2:2] 을 ans 에 추가해줌으로써,
( + ) + ( + ) 이것이 ans 에 들어간다.
따라서 ans는 "()()"이 생긴다.


i :  ()()  | len(i) :  4  | j :  0  | ans {'(())()'}
i :  ()()  | len(i) :  4  | j :  1  | ans {'()()()', '(())()'}
i :  ()()  | len(i) :  4  | j :  2  | ans {'()(())', '()()()', '(())()'}
i :  ()()  | len(i) :  4  | j :  3  | ans {'()(())', '()()()', '(())()'}
i :  (())  | len(i) :  4  | j :  0  | ans {'(()())', '()(())', '()()()', '(())()'}
i :  (())  | len(i) :  4  | j :  1  | ans {'()(())', '()()()', '((()))', '(())()', '(()())'}
i :  (())  | len(i) :  4  | j :  2  | ans {'()(())', '()()()', '((()))', '(())()', '(()())'}
i :  (())  | len(i) :  4  | j :  3  | ans {'()(())', '()()()', '((()))', '(())()', '(()())'}



"""
    
   


        
        
        
