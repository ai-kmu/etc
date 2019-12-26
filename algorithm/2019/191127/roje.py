def solution(begin,target,words):
    ans_cnt = 0
    if target not in words:
        ans_cnt = 0
    else:
        while(len(words)!=0):
            for word in words:
                count=0
                for i in range(len(begin)):
                    if begin[i]!=word[i]:
                        count+=1
                    if count==2:
                        break
                if count==1:
                    temp = word
                    words.remove(word)
            ans_cnt+=1
            if target == temp:
                return ans_cnt
            else:
                begin=temp
    return ans_cnt
