import re

final_cases = list()                                      # 최종 밴 경우의 수를 넣을 리스트

def dfs( my_set, possible_list, order, ban_len):          # 가능한 경우의 수에서 최종 밴 경우들을 찾아냄
    for uid in possible_list[order]:                      # 현재 순서(order)의 밴 가능한 id 순서대로 넣기
        if uid not in my_set:                             # set에 uid가 있는지 확인(.add 사용했을때 리턴 x)
            my_set.add(uid)                                 # uid가 없으면 set에 삽입
            if order == ban_len-1:                          # 이번(order)이 마지막 순서인 경우 확인
                if my_set not in final_cases:                   # 최종 밴 경우의 수에 현재 set이 있는지 확인
                    final_cases.append(my_set.copy())               # 없으면 넣어줌
                my_set.remove(uid)                              # dfs 종료이므로 set에서 이번 uid 다시 제거
                continue                                    # 마지막 순서인 경우는 dfs 종료
            dfs(my_set, possible_list, order+1, ban_len)  # 다음 순서로 dfs 진행
            my_set.remove(uid)                            # 현재 uid로 가능한 dfs 종료. set에서 uid 제거
            
        
def solution(user_id, banned_id):
    answer = 0
    ban_len = len(banned_id)                              # banned_id의 수 저장
    
    w = '\w'                                              # 정규식 [a-zA-Z0-9_]과 동일
    possible_list = list()                                # 밴 리스트마다 가능한 경우의 수 넣어줄 리스트
    
    for bid in banned_id:                                 # 밴id마다 가능한 경우의수 검색
        length = len(bid)                                 # 현재 bid의 길이 저장
        bid = re.compile(bid.replace('*',w,8))            # '*'를 '\w'로 대체
        temp = list()                                     # 저장할 임시 리스트
        for uid in user_id:                               # 모든 id 검색
            if bid.match(uid) and length == len(uid):     # 일치하는지, 길이 같은지 검사
                temp.append(uid)                            # 일치하면 temp에 삽입
        possible_list.append(temp)                        # 검색된 id 리스트를 저장
    

    my_set = set()
    dfs(my_set, possible_list, 0, ban_len)                # dfs 탐색
        
    
    answer = len(final_cases)                             # dfs 종료 후 찾은 최종 경우의 수 
    
    return answer
