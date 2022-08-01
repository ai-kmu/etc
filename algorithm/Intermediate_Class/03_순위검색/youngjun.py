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
        q_order, q_value = query_temp[:-1], int(query_temp[-1])
        for _ in range(3):
            q_order.remove('and')
        q_case = ''.join(q_order)
        if q_case in info_dict.keys():
            score_list = info_dict[q_case]
            score_target = q_value
            score_length = len(score_list)
            low, high = 0, len(score_list)
            while low < high:
                mid = (low + high) // 2
                if score_target > score_list[mid]:
                    low = mid + 1
                elif score_target <= score_list[mid]:
                    high = mid
            q_num = score_length - high
            answer.append(q_num)
        else:
            answer.append(0)
            
    return answer
