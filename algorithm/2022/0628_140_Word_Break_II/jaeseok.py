# bottom-up 방식의 dp 사용
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        size = len(s)
        
        # dp 테이블 초기화. s의 최대 크기를 고려해서 21로 설정
        dp = [[] for i in range(21)]
        # 0글자인 경우
        dp[0] = ['']
        
        # s를 탐색하면서 wordDict에 존재하는 단어가 있는지 확인.
        # i가 커질수록 높은 str에서 줄여가면서 word가 있는지 탐색
        for i in range(1,size+1):
            for j in range(0,i):
                word = s[j:i]
                # word가 wordDict에 있을 경우
                if word in wordDict:
                    # 현재 word 전까지의 이어붙일 단어(들)(여기서는 d에 해당됨)를 dp 테이블에서 찾음
                    for d in dp[j]:
                        # 만약에 해당하는 d가 없다면 word는 첫 번째로 break하는 단어이므로 바로 추가
                        if not d:
                            dp[i].append(word)
                        # 이어붙일 단어(들)가 있다면 그 단어들에 이어서 dp에 추가
                        else:
                            dp[i].append(d + ' ' + word)
        
        # s의 크기에 해당하는 dp 위치에서 word break가 완료
        return dp[size]
