class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                string = []
                num = []
                
                while stack:
                    char = stack.pop()
                    
                    if char.isdigit():
                        num.insert(0, char)
                        print("number", num)
                    
                    elif char != '[':
                        string.insert(0, char)
                        print("string",string)
                
                gob = ''.join(num)
                gob = int(gob)
                string *= gob
                for j in string:
                    stack.append(j)
                
            else:
                stack.append(c)                    
        
        answer = ''.join(string)
        return answer
