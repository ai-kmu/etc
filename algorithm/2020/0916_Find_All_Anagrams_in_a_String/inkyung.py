import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p_cnt = collections.Counter(p)
        s_cnt = collections.Counter(s[:len(p)])
        answer = list()
        i = 0
        j = len(p)
        
        while j <= len(s):
            if s_cnt == p_cnt:      # anagram인 경우
                answer.append(i)

            s_cnt[s[i]] -= 1        # 윈도우를 움직이기 위해서 앞쪽부터 제거
            if s_cnt[s[i]] <= 0:    
                del s_cnt[s[i]]
                
            if j < len(s):          # 끝에 도달하기 전까지 다음 char에 대한 cnt += 1
                 s_cnt[s[j]] += 1
            j += 1
            i += 1
            
        return answer  
