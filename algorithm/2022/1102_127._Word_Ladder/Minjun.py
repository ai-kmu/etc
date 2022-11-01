from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # trivial case
        if endWord not in wordList:
            return 0
        
        # hash를 안 하면 터짐, ,
        wordSet = set(wordList)
        
        # 단어 생성용
        alphabet = 'abcdefghijklmnopqurstuvwxyz'
        
        l = len(beginWord)
        
        # 시작 단어에서 한 단어만 바꾼 모든 단어 생성
        def make_word(w):
            candidate = set()
            for i in range(l):
                for c in alphabet:
                    candidate.add(w[:i] + c + w[i+1:])
            return candidate
    
        Q = deque()
        Q.append((beginWord,1))
        
        while(Q):
            now, cnt = Q.popleft()
            
            if now == endWord:
                return cnt
            
            # 후보군 생성
            wordCandidate = make_word(now)
            
            # 가능한 후보군만 남기기
            wordCandidate = wordCandidate & wordSet
            
            for word in wordCandidate:
                Q.append((word,cnt+1))
                wordSet.remove(word)
        
        return 0
