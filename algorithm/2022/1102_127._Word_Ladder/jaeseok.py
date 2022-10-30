# 오답, time limit
# wordList를 순회하면 무조건 time limit에 걸리도록 문제를 설계한 듯 함

from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 두 단어가 문자가 하나만 차이나는지 확인
        def chk(w1, w2):
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
                    if count > 1:
                        return False
            else:
                return True
        # 정답을 만들 수 없는 예외케이스 제거
        if endWord not in wordList:
            return 0
        q = deque()
        v = defaultdict(int)
        q.append((beginWord, 1))
        v[beginWord] += 1
        # wordList를 순회하면서 조건을 만족하면서 wordlist에 이미 있는 단어는 보지 않도록 함
        while q:
            word, l = q.popleft()
            for i in wordList:
                if chk(word, i) == True and i not in v:
                    # 맨 처음 endWord에 도달한 word가 최소 거리
                    if i == endWord:
                        return l + 1
                    v[i] += 1
                    q.append((i, l+1))
        # 모든 가능한 경우를 다 계산하게 된 경우에는 endWord에 도달하지 못하는 경우이므로 0을 리턴
        return 0

# 찾아본 정답 코드
# word를 순회하면서 반복을 최소화하고, wordList를 set으로 만들고, visited의 역할을 wordList에서 본 word를 제거함으로서 시간을 줄임


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 정답을 만들 수 없는 예외케이스 제거
        if endWord not in wordList:
            return 0
        q = deque()
        # wordList의 접근 시간 복잡도를 줄이기 위해 set으로 변경
        wordList = set(wordList)
        q.append((beginWord, 1))
        while q:
            word, l = q.popleft()
            for i in len(word):
                # word에서 자리를 바꿔가면서 word를 바꿔서 만들 수 있는 가능한 모든 word의 경우를 대입해가면서 wordList에 있는지 확인
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    # 맨 처음 endWord에 도달한 word가 최소 거리
                    if new_word == endWord:
                        return l + 1
                    # 정답은 아니지만 wordList에 word가 있는 경우에는 1 증가된 거리와 함께 큐에 추가
                    if new_word in wordList:
                        q.append(new_word, l+1)
                        # 새로 도달한 word는 wordList에서 그 단어를 지워줌으로서 중복을 피함
                        wordList.remove(new_word)
        # 모든 가능한 경우를 다 계산하게 된 경우에는 endWord에 도달하지 못하는 경우이므로 0을 리턴
        return 0
