from bisect import bisect_left

def solution(info, query):
    applicants = []
    for i in info:
        applicants.append(i.split(' '))

    # trie구조 만들기
		# score만 list 나머지는 dictionary
    applicants_tpye = {}
    for applicant in applicants:
        base_dict = applicants_tpye
        for i, condition in enumerate(applicant[:-1]):    
            if condition not in base_dict:
                if i != 3:
                    base_dict[condition] = dict()
                    base_dict = base_dict[condition]
                else:
                    base_dict[condition] = []
                    base_dict[condition].append(int(applicant[i+1]))
                    base_dict[condition].sort()  # bisect 를 위한 정렬
            elif condition in base_dict:
                if i != 3:
                    base_dict = base_dict[condition]
                if i == 3:
                    base_dict[condition].append(int(applicant[i+1]))
                    base_dict[condition].sort()  # bisect 를 위한 정렬
    
    # print(applicants_tpye)
    
    # 탐색함수 정의
    def explore(base_dict = applicants_tpye, idx=0):
        nonlocal cur_query_type
        condition = cur_query_type[idx]

				# score를 탐색할때는 bisect_left를 이용 
        if idx == 4:             
            return len(base_dict) - bisect_left(base_dict, int(condition))

				# '-'일때는 모두탐색
        if condition == '-':
            sum_app = 0
            for k in base_dict.keys():
                sum_app += explore(base_dict[k], idx+1)
            return sum_app
				# 찾는값이 없으면 0 return
        elif condition not in base_dict:
            return 0
				# 나머지 경우는 일반탐색
        else:
            return explore(base_dict[condition], idx+1) 
    
		# 각각의 query에 대해서 탐색
    answer = []
    for q in query:
        q = q.split(' ')
        cur_query_type = [q[0], q[2], q[4], q[6], q[7]]
        answer.append(explore())
        
    return answer
