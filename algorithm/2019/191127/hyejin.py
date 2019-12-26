
def solution(begin, target, words):
    answer = 0
    #target이 words안에 없을 경우
    if target not in words:
        return answer
    
    stack = [begin]
    while len(words) != 0:
        for i in stack:
            temp_stack = []
            for word in words:
                temp_count =0
                for j in range(len(i)):
                    if word[j] != i[j]:
                        temp_count +=1
                    if temp_count ==2:
                        break
                if temp_count ==1:
                    #기준 word를 stack에 추가
                    temp_stack.append(word)
                    #words에서 방문한 word 제거
                    words.remove(word)
        answer +=1
        if target in temp_stack:
            return answer
        else: 
            stack = temp_stack
    return 0
    

