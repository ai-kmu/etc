#dynamic programming 사용
'''
s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
일 때,
-> pine / applepenapple -> pine / apple / penapple -> pine / apple / pen / apple
                        -> pine / applepen / apple
-> pineapple / penapple -> pineapple / pen / apple
으로 만들 수 있음
따라서 마지막 단어가 wordDict에 있는지 확인, 저장한 이후 다시 거꾸로 나머지 단어들을 저장하는 방식이 필요하다.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def wordfunction(sub):
            
            wordlist = []
            
            #i를 늘려가면서 탐색한다.
            for i in range(len(sub)):
                #i를 늘려가면서 탐색했을 때 발견할 수 있는 단어를 word라 가정할 때
                word = sub[:i+1]
                #word가 wordDict 안에 있는 단어이다.
                if word in wordDict:
                    #word == sub라면 바로 wordlist에 넣거나
                    #혹은 재귀 상황에서 마지막 단어를 추가하고 재귀 정지
                    if word == sub:
                        wordlist.append(word)
                    else:
                        #word를 제외한 나머지 문자열을 가지고 재귀함수 실행
                        #restwords에 마지막 단어 전, 계속 나눠왔던 단어들 저장 후 문자열 생성
                        restwords = wordfunction(sub[i+1:])
                        #print(restwords)
                        for phrase in restwords:
                            wordlist.append(word + " " + phrase)
            return wordlist
        
        return wordfunction(s)
