class Solution:
    def lengthOfLongestSubstring(self, s):
        start_idx = 0
        end_idx = 0
        answer = 0
        longest_ans = 0
        if len(s) < 2:
            return len(s)

        while(True):
            if s[end_idx + 1] not in s[start_idx:end_idx+1]:
                end_idx +=1
                answer +=1
            else:
                start_idx +=1
                answer -=1
            if answer > longest_ans:
                longest_ans = answer
            if end_idx ==len(s)-1:
                break
        return longest_ans + 1
        
