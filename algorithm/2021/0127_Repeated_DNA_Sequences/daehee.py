class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        output = []
        dt = collections.defaultdict(int)   # 0으로 초기화되는 dict 선언
        
        for i in range(length-9):           # 10개의 string 모두 횟수 세기
            dt[s[i:i+10]] += 1              
        
        for i in dt:                        # 2번 이상 나온 substring output에 추가
            if dt[i]>1:
                output.append(i)
                
        return output                
