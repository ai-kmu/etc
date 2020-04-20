import copy

def solution(user_id, banned_id):
    user_id_dict = {}
    banned_id_dict = {}
    answer_list = []
    # user_id를 길이에 따라 저장
    for i in user_id:
        if len(i) in user_id_dict:
            user_id_dict[len(i)] += [i]
        else:
            user_id_dict[len(i)] = [i]
    # ban_id를 길이에 따라 저장
    for i in banned_id:
        if len(i) in banned_id_dict:
            banned_id_dict[len(i)] += [i]
        else:
            banned_id_dict[len(i)] = [i]
    # 같은 길이 중 user의 수와 ban된 user의 수가 같은 경우에는 경우의 수가 1이기 때문에 1을 저장
    for i in banned_id_dict:
        if len(banned_id_dict[i]) == len(user_id_dict[i]):
            answer_list.append(1)
        # 길이가 다른 경우에는 ban된 id에 따른 user를 index로 저장
        else:
            user_id_list = user_id_dict[i]
            banned_id_list = banned_id_dict[i]
            ban_list = []
            for i in banned_id_list:
                ban = []
                for j in user_id_list:
                    if check_id(j, i):
                        ban.append(user_id_list.index(j))
                ban_list.append(ban)
            answer_num = []
            # 만약 ban된 id에 따른 user가 1명이라면 경우의 수가 1이기 때문에 삭제
            for i in ban_list:
                if len(i) == 1:
                    ban_list.remove(i)
                    answer_num += i
            ban_user_list = []
            # ban된 id에 따른 user가 1이 아닌 경우에는 경우의 수를 계산
            for i in ban_list:
                ban_user_list = return_id_num(ban_user_list, i, answer_num)
            if ban_user_list:
                answer_list.append(len(ban_user_list))
    # 경우의 수를 모두 곱해준다
    answer = answer_list[0]
    for i in range(1, len(answer_list)):
        answer *= answer_list[i]
    return answer


# banned_id마다 제재될 수 있는 사용자를 찾는 함수
def check_id(user, banned): 
    if len(user) != len(banned):
            return False
    for i in range(len(banned)):
        if banned[i] == '*':
            continue
        elif banned[i] == user[i]:
            continue
        else:
            return False
    return True


# ban될 수 있는 경우의 수를 계산해주는 함수
def return_id_num(ban_user_list, ban_id_num_list, answer_num):
    ban_user_id_list = []
    # ban_user_list에 원소가 있는 경우는 미리 포함된 user를 제외하고 ban될 수 있는 경우를 계산
    if ban_user_list:
        for i in ban_id_num_list:
            if i in answer_num:
                continue
            for j in ban_user_list:
                if i not in j:
                    new_ban_list = j.copy()
                    new_ban_list.append(i)
                    new_ban_list.sort()
                    # 중복 제거
                    if new_ban_list in ban_user_id_list:
                        continue
                    ban_user_id_list.append(new_ban_list)
    # 첫 ban_user_list인 경우는 null이기 때문에 ban_id_num_list를 그대로 넣어줌
    else:
        for i in ban_id_num_list:
            if i in answer_num:
                continue
            ban_user_id_list.append([i])
    return ban_user_id_list
