# Sol 1. info 정보를 hash table로 생성한다.
# query 검색에서 시간초과 발생

from itertools import combinations
from collections import defaultdict

def solution(info, query):
    info_dict = defaultdict(list)
    answer = []
    
    for i in info:
        info_temp = i.split(" ")
        condition, value = info_temp[:-1], int(info_temp[-1])
        for n in range(5):
            combi = list(combinations(range(4),n))
            for c in combi:
                case = ''
                for j in range(4):
                    if j in c:
                        case += condition[j]
                    else:
                        case += '-'
                info_dict[case].append(value)

    for key in info_dict.keys():
        info_dict[key] = sorted(info_dict[key])

    for q in query:
        query_temp = q.split()
        order, value = query_temp[:-1], int(query_temp[-1])
        for _ in range(3):
            order.remove('and')
        q_case = ''.join(order)
        if q_case in info_dict.keys():
            q_num = 0
            for num in info_dict[q_case]:
                if num >= value:
                    q_num += 1
            answer.append(q_num)
        else:
            answer.append(0)
            
    return answer
