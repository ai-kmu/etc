from collections import deque
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # dictionary 만들기
				# dictionary 의 key는 word에서 특정char이 '0'으로 변경된 단어이다
				# dictionary 의 value는 set type으로 '0'을제외한 다른 char이 동일한 단어이다
	
        w_dict = defaultdict(set)
        wordList += [beginWord]

        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + '0' + word[i+1:]
                w_dict[new_word].add(word)
        
				# 최단경로를 찾기위한 BFS
				# BFS는 동일한 단어를 본다면, 이전에 봤을때의 count 가 더 작거나 같음이 보장됨으로,
				# 이미 Q에 추가했던 단어는 Q에 넣지 않는다(Seen 이용)
    
        seen = set([beginWord])
        Q = deque([[beginWord, 0]])

        while Q:

            cur_word, count = Q.popleft()
						
						# 종료조건
            if cur_word == endWord:
                return count + 1

            # 한글자 차이나는 곳을 Q에 추가(봤던 단어는 제외)
            for i in range(len(cur_word)):
                new_word = cur_word[:i] + '0' + cur_word[i+1:]
                for tmp_word in w_dict[new_word]:
                    if tmp_word in seen:
                        continue
                    seen.add(tmp_word)
                    Q.append([tmp_word, count+1])

        return 0
