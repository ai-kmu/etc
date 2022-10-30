from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # case 1. end word 있는지 체크 
        if endWord not in wordList:
            return 0
        # set이 해쉬를 써서 빠르다캄
        wordSet = set(wordList)
    
        # 해쉬를 쓰려면 이웃 단어를 만들어서 찾는 것이 빠를 것
        def neighbor(word):
            res = []
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    res.append(word[:i] + char + word[i+1:])
            return res
        
        # dq 초기화
        dq = deque()
        dq.append((beginWord, 1))
        
        # bfs
        while dq:
            word, step = dq.popleft()
            # 종료조건
            if word == endWord:
                return step
            # 인접 단어 리스트
            res = neighbor(word)
            for data in res:
                if data in wordSet:
                    dq.append((data, step + 1))
                    wordSet.remove(data)
        return 0
        
