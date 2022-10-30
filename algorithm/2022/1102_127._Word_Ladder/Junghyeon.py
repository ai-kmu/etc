'''
Time Limit Exceeded
is_single_diff 함수에서 시간초과가 발생한 것 같음
생각없이 짜다가 구데기 코드가 되어버렸습니다...
'''

from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 두 word를 비교해서 하나 차이가 나면 True를 리턴
        def is_single_diff(s, s2):
            flag = False
            for i, j in zip(s, s2):
                if i != j:
                    # 두개 이상의 차이가 나는 경우
                    if flag: 
                        return False
                    flag = True
            # 하나 차이가 나는 경우
            if flag:
                return True
            return False

        # word의 길이가 1이고 찾고자하는 word가 리스트에 있다면
        if len(beginWord) == 1 and endWord in wordList:
            return 2
        
        deq = deque([[beginWord, 1]])
        flag2 = False
        
        # 방문한 단어를 딕셔너리에 저장
        visited = defaultdict(int)
        visited[beginWord] = 1
        
        # bfs를 이용
        while deq:
            p, cnt = deq.popleft()
            for w in wordList:
                if is_single_diff(p, w) and w not in visited: 
                    flag2 = True
                    if w == endWord:
                        cnt += 1
                        return cnt
                    visited[w] = 1
                    deq.append([w, cnt+1])
        
        # w가 endWord와 다르거나, 한번도 cnt를 증가시키지 못했거나 endWord가 방문한 딕셔너리에 없다면 0을 리턴
        if w != endWord or flag2 == False or endWord not in visited:
            return 0
        
        return cnt
