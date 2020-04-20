"""
우선 와일드카드가 포함된 문자(banned_id)로 가능한 모든 user_id의 idx를 추출한다.
이를 가지고 완전 탐색 방법을 이용하여 답을 구한다
"""

import re

def solution(user_id, banned_id):
    possible_id = []   # 각 banned_id로부터 가능한 user_id들의 index들이 저장될 배열
    cases_arr = []     # 모든 정답들을 저장할 배열
    len_banned_id = len(banned_id)  #

    def calc_cases_idx(id): # 가능한 모든 경우의 수를 추출하는 함수
        id+="$"
        regex = re.compile(id.replace('*', '.'))
        matches = [i for i, string in enumerate(user_id) if re.match(regex, string)]
        return matches
    
    def recSolution(n, arr): #현재 몇번째 banned_id인지, 어떠한 user_id들이 선택되었는지에 대한 배열
        if n == len_banned_id:
            arr.sort()
            if arr not in cases_arr:
                cases_arr.append(arr)
                return 1
            else:
                return 0
        rec_answer = 0
        for num in possible_id[n]:
            if num not in arr:
                rec_answer += recSolution(n+1, arr + [num])
                
        return rec_answer
    
    for i in range(len(banned_id)):
        possible_id.append(calc_cases_idx(banned_id[i]))
    print(possible_id)
    
    
    return recSolution(0, [])
