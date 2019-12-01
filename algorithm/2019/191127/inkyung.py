def solution(begin, target, words):
    begin = [begin]
    answer = 0
    if not target in words:
        return 0
    while len(words) != 0:
        for temp in begin:
            lst = []
            for word in words:
                cnt = 0
                for i in range(len(temp)):
                    #temp와 word를 비교하면서 다른게 있다면 +1
                    if temp[i] != word[i]:
                        cnt += 1
                    #만약 이미 2개가 다르다면 break
                    if cnt == 2:    break
                #한글자만 다르다면 lst에 해당 단어를 추가함
                if cnt == 1:
                    lst.append(word)
                    words.remove(word)
        #lst에 해당 단어를 추가한 이후이기 때문에 1번 변화한 과정
        answer += 1
        #변화한 단어들 중 target이 있다면 끝
        if target in lst:
            return answer
        #변화한 단어들 중에 target이 없다면 만들어 둔 리스트 안에서 다시 반복문 수행
        #리스트 안에는 이전에 추가한 word하나만 존재
        else:
