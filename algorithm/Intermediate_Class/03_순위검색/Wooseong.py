from collections import defaultdict

def solution(info, query):
    # 지원자 정보를 key로 점수 list를 value로 하는 dictionary 생성
    # query로 -도 들어오기 때문에 이것도 추가해서 만듦
    # for문 5중첩이 괴랄하지만 밑 네 개는 총 16개로 고정
    # 그래서 사실상 O(N)
    info_dict = defaultdict(list)
    for case in info:
        case = case.split()
        for lang in [case[0], "-"]:
            for work in [case[1], "-"]:
                for jjam in [case[2], "-"]:
                    for food in [case[3], "-"]:
                        info_dict[lang + work + jjam + food].append(int(case[4]))
    
    # 이진 탐색을 위해 지원자 점수 sorting
    for case in info_dict:
        info_dict[case].sort()
    
    # query 탐색
    answer = []
    for cond in query:
        cond, score = ''.join(cond.split(' and ')).split()
        score = int(score)
        # cand: 해당 조건을 갖는 지원자 점수 list
        cand = info_dict[cond]
        
        # 이진탐색
        persons = len(cand)
        lb = 0
        ub = persons - 1
        under = persons
        while lb <= ub:
            mid = (lb + ub) // 2
            if score <= cand[mid]:
                under = mid
                ub = mid - 1
            else:
                lb = mid + 1
        
        # 이진탐색 결과로 나온 under는
        # score 이상의 최초 index
        answer.append(persons - under)
        
    return answer
