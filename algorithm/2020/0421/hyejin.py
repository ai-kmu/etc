from copy import deepcopy

# 가능한 조합들을 담을 list
check = [] 

# 재귀함수 idx는 현재 index, ban_possible은 가능한 id들
# arr는 현재 만들고있는 조합 set
# ban_len은 banned_id list의 개수
def check_answer(idx, ban_possible, arr, ban_len):
    global check
    # 만든 arr의 개수가 ban list와 같다면 중복검사하고 넣기
    if idx == ban_len:
        if len(arr) == ban_len and arr not in check:
            check.append(deepcopy(arr))
        return
    
    # id가 arr에 들어있지 않다면 추가가능
    for id in ban_possible[idx]:
        if id not in arr:
            arr.add(id)
            check_answer(idx+1, ban_possible, arr, ban_len)
            arr.remove(id)
        

def solution(user_id, banned_id):
    answer = 0
    ban_possible = []
    for i in range(len(banned_id)):
        ban_possible.append(set())
    
    # 각 ban id에 어떤 user id가 가능한지 검사하고 가능한 id는 ban_possibl       e에 넣어주기
    for idx,ban in enumerate(banned_id):
        for user in user_id:
            if len(ban) != len(user):
                continue
            id_equal = True
            # for문을 3번 돌기 때문에 굉장히 비효율적임.
            # character 하나하나 검사하기
            for i in range(len(ban)):
                if '*' == ban[i] or user[i] == ban[i]:
                    continue
                else:
                    id_equal = False
                    break
            if id_equal == True:
                ban_possible[idx].add(user)
    
    # 가능한 조합 찾기
    check_answer(0,ban_possible, set(), len(banned_id))
    return len(check)
