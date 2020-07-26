class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = []
        
        if s == "":
            return 0
        
        temp= []
        substring = []
        
        for ind, char in enumerate(s):
            if char not in temp: # 앞의 temp 문자열에 현재 문자가 존재하지 않으면
                temp.append(char)
            else:  # 앞의 temp 문자열에 현재 문자가 존재한다면
                substring.append(temp)  #앞의 temp 문자열은 리스트에 담는다
                temp2 = temp
                start = temp2.index(char)  
                temp = temp2[start+1:]  # temp 초기화시키고, 앞의 temp 문자열에서 현재 문자 다음의 index부터 새로 temp에 저장
                temp.append(s[ind])  # 현재 문자도 temp에 append
            
            if ind == (len(s)-1):  # 마지막에 남은 temp append
                substring.append(temp)
            
        num_list = []
        for sub in substring:
            num_list.append(len(sub))
        
        return max(num_list)
