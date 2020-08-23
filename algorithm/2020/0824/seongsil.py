class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        answer = ""
        for i in range(numRows):
            ind = i
            while ind < len(s):
                answer += s[ind]  
                ind += (numRows*2 -2)  # 가장 많은 column에 있는 알파벳 인덱스 저장
        
                if i > 0 and i < numRows - 1 and (ind - i*2) < len(s):  # column에 하나만 있는 알파벳 추가
                    answer += s[ind - i*2]
        return answer
