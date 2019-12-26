## sol1
def solution(begin,target,words):
    ans_cnt = 0
    if target not in words:
        return 0
    else:
        while(len(words) != 0):
            for word in words:
                count = 0
                for idx in range(len(begin)):
                    if begin[idx] != word[idx]:
                        count += 1
                    if count == 2:
                        break
                if count == 1:
                    temp = word
                    words.remove(word)
            ans_cnt += 1
            if target == temp:
                return ans_cnt
            else:
                begin = temp
    return ans_cnt

## sol2
def solution(begin,target,words):
    answer = [begin]
    ans_cnt = 0
    if target not in words:
        return 0
    else:
        while(len(words) != 0):
            for start in answer:
                for word in words:
                    count = 0
                    for idx in range(len(start)):
                        if start[idx] != word[idx]:
                            count += 1
                        if count == 2:
                            break
                    if count == 1:
                        answer.append(word)
                        words.remove(word)
                ans_cnt += 1
                if target in answer:
                    return ans_cnt
                else:
                    if ans_cnt == 1:
                        answer.remove(begin)
    return ans_cnt
