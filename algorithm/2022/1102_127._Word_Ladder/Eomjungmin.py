from collections import deque
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # bfs를 위한 deque 선언 후 시작 단어를 레벨과 함께 deque에 추가
        deq = deque()
        deq.append((beginWord, 1))
        
        # 단어 길이 저장
        l = len(beginWord)
        
        # 두 글자가 서로 같은 단어는 같은 그룹에 저장 -> dictionary 이용
        one_letter_change_dict = defaultdict(list)
        for w in wordList:
            for i in range(l):
                one_letter_change_dict[w[:i] + "*" + w[i+1:]].append(w)         
        
        # 방문했던 단어 저장위한 set 선언
        visited = set()
        
        # bfs를 이용하여 정답 출력
        # 현재 단어 word랑 한 글자만 다른 다른 단어들 iword를 뽑아내서
        # iword 안에 있는 단어 하나씩 보면서 그 단어가 endWord랑 같으면 바로 level+1를 return
        # 그렇지 않으면 그 단어를 방문 안한 경우 deq에 추가하고 추가했다면 deq에 추가하지 않도록 함
        # 그리하여 중복 계산을 방지하도록 함
        while deq:
            word, level = deq.popleft()
            for i in range(l):
                iword = one_letter_change_dict[word[:i]+ "*" + word[i+1:]]
                for j in iword:
                    if j == endWord:
                        return level + 1
                    else:
                        if j not in visited:
                            visited.add(j)
                            deq.append((j, level+1))
                            
        return 0
                            
                
            
            
        
        
        
