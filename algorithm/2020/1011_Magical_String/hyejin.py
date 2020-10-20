class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        
        # magic string 배열
        magic_s = []
        # 현재 패턴의 숫자
        magic_int = 1
        # 다음 패턴에서 1 => 2, 2=> 1로 바뀌어야함.
        shift = {1: 2, 2: 1}
        
        # magic_string에서 현재 맞춰야되는 length의 index
        current_length_idx = 0
        
        while len(magic_s) < n:
            # 현재 패턴의 숫자를 넣어줌
            magic_s.append(magic_int)
            
            # 만약 맞춰야되는 length가 2라면 한번더 넣어줌.
            if magic_s[current_length_idx] == 2:
                magic_s.append(magic_int)
            
            # magic int를 바꿔줌.
            magic_int = shift[magic_int]
            
            # 맞춰야되는 length를 업데이트
            current_length_idx += 1
       
        # 1 카운트 하기
        answer = 0
        for i in magic_s[:n]:
            answer += 1 if i == 1 else 0
        
        return answer
