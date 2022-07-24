class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 만약 숫자가 없다면 []를 return 예외처리
        if not digits:
            return []
        # 각 번호에 알파벳 할당
        number = {"2": "abc", 
                  "3": "def", 
                  "4": "ghi", 
                  "5": "jkl", 
                  "6": "mno", 
                  "7": "pqrs", 
                  "8": "tuv", 
                  "9": "wxyz"}
        
        # 정답을 위한 res와 dfs를 위한 stack
        res = []
        stack = []
        
        # dfs 정의
        def dfs():
            # 현재 만든 문자들의 길이를 index로 설정
            index = len(stack)
            
            # 만약 현재 만든 문자들의 길이가 digits와 같다면
            # dfs로 자식노드를 모두 탐색한 것이기 때문에 결과에 더해준다
            if index == len(digits):
                res.append(''.join(stack))
                return
            
            # 현재 숫자는 index를 통해 digits에서 하나씩 가져온다
            digit = digits[index]
            
            # 현재 숫자에 해당하는 알파벳을 루프를 돌며 stack에 차례로 넣어주고
            # dfs를 수행
            # 이후 stack.pop을 통해 이미 탐색한 알파벳을 빼준다
            for c in number[digit]:
                stack.append(c)
                dfs()
                stack.pop()
                
        dfs()
        return res
