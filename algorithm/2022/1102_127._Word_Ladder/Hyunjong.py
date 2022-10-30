# 문제 못 풀어서 정답 코드 봤어요
# bfs 식 구현
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # set으로 경로 확인
        # set에서 간 경로이면 하나씩 제거하는 방식
        # 최소가 보장되어야 하기 때문에 동작 가능
        s = set(wordList)

        # 모든 알파벳 리스트
        l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z']

        queue=deque([])
        queue.append([beginWord, 0])

        while queue:
            word,count =queue.popleft()

            # 큐에서 뽑은 단어가 마지막 단어이면 종료
            if word == endWord:
                # 시작을 0으로 했으므로 +1
                return count + 1
            # 뽑은 단어에 하나씩 알파벳을 넣어가면 비교
            for j in range(len(word)):
                for i in l:
                    # 만든 단어가 set에 있고(아직 방문한 적 없고), 시작 단어가 아니면
                    if (word[:j]+i+word[j+1:]) in s and (word[:j]+i+word[j+1:]) != beginWord:
                        # set에서 만든 단어를 제거하고
                        s.remove(word[:j]+i+word[j+1:])
                        # queue에 만든 단어와 count+1 append
                        queue.append([word[:j]+i+word[j+1:], count+1])
        # 답이 없으면 return 0
        return 0
