class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence = set() # 문자 10개씩 저장하는 sequence 집합 생성
        repeat_sequence = set() # sequence안 요소들 중 반복되는 요소 저장하는 집합 생성

        for i in range(len(s)-9):
            current = s[i:i+10] # s 리스트에서 i순서대로 문자 10개씩 current에 저장
            if current in sequence: # 현재 current 문자 10개 요소가 sequence에 이미 있다면
                # 반복되는 것이므로 repeat_sequence에 저장
                repeat_sequence.add(current)

            sequence.add(current) # 현재 current를 항상 sequence에 저장
            
        return repeat_sequence
