class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # string과 wordDict이 주어짐. wordDict대로 s에 스페이스를 추가해라
        
        def dfs(s):
            word_arr = [] # 
            for idx in range(len(s)): # wordDict에 있는 word까지 계속 체크
                curr_word = s[:idx+1]
                left_s = s[idx+1:]
                if curr_word in wordDict: # 만약 현재 자른 word가 wordDict에 있으면 추가.
                    if not left_s:
                        word_arr.append([curr_word]) # 마지막이면 넣고 끝내기
                    for word in dfs(left_s): # 나머지 string으로 dfs 수행
                        word_arr.append([curr_word] + word)
                        
            return word_arr
    
        return [" ".join(words) for words in dfs(s)] # 가능한 모든 경우 계산
