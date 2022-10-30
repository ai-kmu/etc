from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        asciis = string.ascii_lowercase  # 'abcde ~ xyz'의 문자열임
        wordList = set(wordList)  # set으로 변환
        bfs = deque()  # bfs로 데크 사용
        
        bfs.append((beginWord, 1))
        
        while bfs:
            
            word, depth = bfs.popleft()
            
            if word == endWord:  # 만약 도달하면 return depth
                return depth
            
            for i in range(len(word)):
                for j in asciis:  # 모든 ascii lower case 중에서
                    next_word = word[:i] + j + word[i+1:]
                    if next_word in wordList:  # wordList에 존재하면 
                        bfs.append((next_word, depth + 1))  # 다음 방문할 목록에 추가함
                        wordList.remove(next_word)  # 방문했다면 
        
        return 0
