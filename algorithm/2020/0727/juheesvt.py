class Solution:
   
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        # substring의 길이 중 가장 긴 것을 return 해주는 함수
        def maxLengthAmongElementsOfArray(substring: list) -> int:
        
            length = list()
            for i in range(len(substring)):
                length.append(len(substring[i]))
        
            return max(length)
 
        if s == "":
            return 0
        
        
        i = 0          
        j = i           
        length = len(s)
        substring = ["" for i in range(length)]       # substring의 각 자리에는 문자열 s에서 해당 인덱스까지의 longest substring이 저장된다
        
        while i < length:
            print(substring[i], "/n/n")
            while (j < length) and (substring[i].find(s[j]) == -1) :    # 같은 문자가 나오지 않을 때까지 계속 문자열에 더함 !!
                substring[i] += s[j]
                j += 1
                print(substring[i])
            i += 1
            j = i
            
            
            
        return maxLengthAmongElementsOfArray(substring)
    
    
        
            
