class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 정답 리스트
        word_list = [] 
        # 문장에 다음 단어를 추가할 때 시간 절약을 위해 wordDict 안 단어 중 가장 긴 단어의 길이를 저장
        max_word_len = max([len(i) for i in wordDict])
        
        # dfs 탐색: word가 딕셔너리에 포함되면 그 순간의 인덱스를 이용해서 계속 dfs탐색.
        # 탐색 다 했으면 backtracing을 위해 path에서 pop시켜야 한다.
        # s: 문제에서 주어진 입력 s
        # sentence: 일종의 문장 path
        # start: dfs에서 s의 시작할 인덱스
        def dfs(s,sentence,start):
            # s의 끝까지 다 탐색했으면 정답 리스트에 append해서 저장
            if start == len(s):
                word_list.append(" ".join(sentence))
            
            # 주어진 인덱스 start부터 최대 길이 만큼 다음 단어 탐색
            for i in range(start,max_word_len+start):
                if i >= len(s):
                    break
                word = s[start:i+1]
                if word in wordDict:
                    sentence.append(word)
                    dfs(s,sentence,i+1) # dfs 탐색
                    sentence.pop()
                    
        dfs(s,[],0)    
        
        return word_list
