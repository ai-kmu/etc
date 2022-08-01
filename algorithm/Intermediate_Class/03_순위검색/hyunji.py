# 오답
import re

def solution(info, query):
    answer = []
    
    # query를 dictionary 형태로 바꿔줌
    # 조건은 key, 점수는 value
    que = []
    query_dict = {}
    for q in query:
        remove_q = re.sub("and ", '', q)
        remove_q2 = re.sub("-", '', remove_q)
        tmp = remove_q2.split(" ")
        
        que.append(tmp)
    
    for q in que:
        tmp = ''
        for i in range(4):
            tmp += q[i]
        query_dict[tmp] = int(q[4])
    
    # print(query_dict)
    
    # info를 dictionary 형태로 바꿔줌
    info_dict = {}
    info_list = []
    for i in info:
        tmp = i.split(" ")
        info_list.append(tmp)
        
    for information in info_list:
        tmp = ''
        for j in range(4):
            tmp += information[j]
        info_dict[tmp] = int(information[4])
        
    # print(info_dict)
    for que in query_dict.keys():
        cnt = 0
        for information in info_dict.keys():
            if query_dict[que] <= info_dict[information]:
                if que in information:
                    cnt += 1
                    
        answer.append(cnt)
    
    return answer
