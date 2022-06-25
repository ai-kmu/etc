class Solution(object):
    def wordBreak(self, s, wordDict):

        answer = []
        max_len = len(max(wordDict, key=len)) #  diconary에 있는것중 최대길이
        
        # 한글자씩 보면서 word에 추가
        # word가 만들어지면 output에 추가
        # output이 s의 모든 word를 포함하면 answer에 추가
        
        # i : s의 index
        # word : 현재까지의 단어
        # dictionary에 있는 단어들의 조합(answer의 원소)
        def find_s(i, word, output):   
            # 최대 길이를 넘으면 현재 word값이 dictionary에 있는지 확인하고 종료
            if i >= len(s):
                if word in wordDict:
                    answer.append(output + word)
                return
            
            # word가 dictionary안의 최대 길이보다 길어지면 종료
            if len(word) > max_len:
                return

            # word가 wordDict안에 있으면 output에 추가
            for word_in_dict in wordDict:
                if word == word_in_dict:
                    tmp_output = output + word + " "
                    find_s(i, "", tmp_output)
            
            # index 1 증가
            find_s(i+1, word + s[i], output)
        
        find_s(0, "", "")
        
        return answer
