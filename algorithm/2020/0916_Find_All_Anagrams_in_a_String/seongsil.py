import collections 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:  
        answer = []
        start = 0
        
        if len(s) < len(p):
            return answer
        
        dCount = collections.Counter(p)  # 정렬하는데 메모리 많이쓰이므로 카운터 함수 사용
        sub_sCount = collections.Counter(s[start: len(p)-1]) 
        
        for end in range(len(p)-1, len(s)):  # 3개씩 보면서 카운터 수 비교
            
            sub_sCount[s[end]] += 1
            if dCount == sub_sCount:
                answer.append(start)
            
            sub_sCount[s[start]] -= 1
            
            
            if sub_sCount[s[start]] == 0:
                del sub_sCount[s[start]]
                
            start += 1
                
        return answer
