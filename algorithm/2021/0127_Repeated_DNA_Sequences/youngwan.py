class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = []                                  # 정답 리스트
        seq_dict = collections.defaultdict(int)   # 10개의 string 마다 저장할 dictionary
        for i in range(len(s) - 9):               # 10개의 string마다
            seq_dict[s[i:i+10]] += 1              # dictionary에 추가      
        for in_seq in seq_dict:                  
            if seq_dict[in_seq] >= 2:             # dictionary에 나타난 숫자가 2개 이상인 경우
                seq.append(in_seq)                # 정답에 추가        
        return seq
