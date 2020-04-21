## user_id를 길이별로 인덱스 저장하여 조합을 이용해 풀려고 했으나 몇몇 케이스에서 실패가 뜸
## 오늘 이후 다시 풀어 올릴 예정
import operator as op
from functools import reduce

# 조합 개수 수식
def nCr(n, r):
    if n < 1 or r < 0 or n < r:
        raise VAlueError
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

# ban_id에 해당하는 지 검사하는 함수
def checkToBan(user, ban_id):
    for _ in range(len(ban_id)):
        if ban_id[_] == '*':
            continue
        else:
            if ban_id[_] == user[_]:
                continue
            else:
                return False
    return True
                
    
def solution(user_id, banned_id):
    answer = {}
    id_dic = {}
    # banned_id의 중복개수 저장
    overlap = {}
    user_dic = {}
    
    for i in banned_id:
        try: overlap[i] += 1
        except: overlap[i] = 1
    
    # user_id를 길이별로 인덱스 저장
    for i, user in enumerate(user_id):
        if len(user) in id_dic:
            id_dic[len(user)].append(i)
        else:
            id_dic[len(user)] = [i]
    
    for b_idx, ban_id in enumerate(banned_id):
        count = 0
        # ban_id의 길이가 id_dic에 있다면
        if len(ban_id) in id_dic:
            for i in id_dic[len(ban_id)]:
                if checkToBan(user_id[i], ban_id):
                    count += 1
                    try: user_dic[user_id[i]].append(b_idx)
                    except: user_dic[user_id[i]] = [b_idx]
            answer[ban_id] = count
        
        # ban_id의 길이가 없다면
        else:
            continue
    
    # 결과 계산
    result = 1
    for item in answer:
        result *=  nCr(answer[item], overlap[item])
    # print(overlap)
    # print(answer)
    print(user_dic)
    return result
