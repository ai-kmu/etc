class Solution:

    def longestPalindrome(self, s: str) -> str:
        s_answer = 0 # 시작 index
        e_answer = 0 # 끝 index
        s_length = len(s) # string 길이
        
        for start in range(s_length):
            # 검사할 길이보다 답이 더 길면 끝냄.
            if s_length-1 - start < e_answer - s_answer:
                break
            
            # 끝에서부터 palindrome 검사
            for end in range(s_length, start, -1):
                sub_string = s[start:end]
                if sub_string[::-1] == sub_string: # 뒤집은 것과 비교
                    curr_start, curr_end = start, end-1
                    break
                    
            # 기존 answer와 비교
            if e_answer - s_answer < curr_end - curr_start:
                s_answer, e_answer = curr_start, curr_end
    
                
        return s[s_answer:e_answer+1]
