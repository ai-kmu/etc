
cnt = 0
comp = set()

def compare(s1, s2) :                                                        # user가 불량사용자랑 매칭되는지 체크하는 함수

    if len(s1) != len(s2) :                                                  # 길이가 맞지 않으면 False 리턴
        return False

    for i in range(len(s1)) :
        if s1[i] == s2[i] or s2[i] == '*' :                                  # 불량사용자랑 매칭되는지 체크 중
            continue
        else :
            return False                                                     # 한번이라도 다르면 False 리턴!
    return True


def find(set, target) :                                                       # set 에서 특정 요소 값의 존재 여부를 반환하는 함수

    temp = list(set)                                                          # 인덱싱을 위해 set을 list로 변환해준다.

    for i in range(len(temp)) :
        if temp[i] == target :
            return True

    return False


def dfs(idx, check_set, candidate_list) :                                     # dfs를 돌면서 매칭되는지 체크하기

    global cnt

    if idx == len(candidate_list) :
        if len(check_set) == len(candidate_list) :
            for i in range(len(comp)) :
                temp_comp = list(comp)
                if temp_comp[i] == check_set :
                    return
            cnt += 1
            comp.update(check_set)
        return

    for candidate in range(len(candidate_list[idx])) :
        if find(check_set,candidate_list[idx][candidate]) == False :
            check_set.add(candidate_list[idx][candidate])
            dfs(idx+1, check_set, candidate_list)
            check_set.remove(candidate_list[idx][candidate])

def solution(user_id, banned_id):

    candidate_list = []
    user_id_len = len(user_id)
    banned_id_len = len(banned_id)

    for ban in range(banned_id_len) :
        temp = []
        for user in range(user_id_len) :
            if compare(user_id[user], banned_id[ban]) == True :              # 길이가 맞는 것 끼리 하나의 리스트로 묶는다 (temp)
                temp.append(user_id[user])

        candidate_list.append(temp)                                           # candidate_list안에 있는 각 list안의 요소들은 길이가 같다.

    check = set()
    dfs(0, check, candidate_list)                                             # dfs ㄱㄱ링

    return cnt



