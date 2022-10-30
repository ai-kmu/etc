# Time Limit...ㅠㅠ

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        q = deque()
        q.append((beginWord, 1))
        visited = []
        dict = {}
        wordList1 = wordList + [beginWord]
        
        # wordList의 element들에서 서로 겹치는 알파벳이 하나라도 존재하는 단어들을 딕셔너리로 정리
        for word1 in wordList1:
            dict[word1] = []
            for word2 in wordList1:
                cnt = 0
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        cnt += 1
                
                if cnt == 1:
                    dict[word1] += [word2]
        
        while q:
            now, cnt = q.popleft()
            visited.append(now)
            # endWord랑 지금 단어가 같으면 return
            if now == endWord:
                return cnt
            
            # now 단어와 겹치는 알파벳이 하나라도 있는 단어들 list
            for i in dict[now]:
                if i not in visited:
                    q.append([i, cnt+1])
        
        return 0
        
