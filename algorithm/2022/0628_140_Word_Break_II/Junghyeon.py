class Solution:
    '''
    DFS를 이용해서 슬라이싱한 s가 wordDict에 있을때마다 탐색 진행
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def DFS(s, tmp):
            # 탐색을 마치면 word_list 배열에 저장
            if len(s) == 0:
                word_list.append(tmp)
            # wordDict에서 단어를 꺼내 s를 슬라이싱 한것과 비교
            for word in wordDict:
                if s[:len(word)] == word:
                    DFS(s[len(word):], tmp+[word])
        
        result = list()
        tmp = list()
        word_list = list()
                    
        DFS(s, tmp)
        
        # word_list에 있는 단어들을 합쳐주는 작업
        for words in word_list:
            result.append(' '.join(words))
    
        return result
