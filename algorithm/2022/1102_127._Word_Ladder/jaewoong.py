class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        # 예외처리
        if endWord not in wordList: 
            return 0
        # BFS 
        curr_level = {beginWord}
        dist = 1
        while curr_level:
            # 있는 단어 하나씩 빼줌
            wordList -= curr_level
            next_level = set()
            for word in curr_level:
                # 단어를 하나씩 변경해봄(BFS)
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        # 마지막 원하는 단어를 찾았을 때는 아예 같은 집합형태
                        if new_word == endWord:
                            return 1 + dist
                        # 비어있진않지만 있는 경우는 in으로
                        if new_word in wordList:
                            next_level.add(new_word)
            curr_level = next_level
            dist += 1
        return 0
        
