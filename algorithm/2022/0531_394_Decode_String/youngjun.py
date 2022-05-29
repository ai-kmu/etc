class Solution:
    def decodeString(self, s: str) -> str:
            num = 0
            stack = []
            
            for ch in s:
                # 숫자의 경우, num에 저장한다.
                while ch.isdigit():
                    num = num * 10 + int(ch)

                
            return answer
