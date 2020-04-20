from itertools import product

def solution(user_id, banned_id):
    answer = 0
    isbaned = [[] for i in range(len(banned_id))] # 각 banned_id에 매치되는 user_id 저장할 list
    for bidx, ban in enumerate(banned_id):  # 각 banned_id 에 해당하는 user_id 구하기
        idxlist = []
        idx = -1
        banlen = len(ban)
        while True:
            idx = ban.find('*',idx+1)
            idxlist.append(idx)
            if idx == -1:
                break;
        banpossible = []
        for useridx,user in enumerate(user_id):
            if banlen == len(user):
                temp = list(user)
                for i in range(len(idxlist)-1):
                    temp[idxlist[i]] = '*'
                temp = ''.join(temp)
                if temp == ban:
                    banpossible.append(useridx)                    
        isbaned[bidx] = banpossible
            
    alllist = list(product(*isbaned))   # 각 banned_id 에 해당하는 user_id들을 조합
    lastlist = []
    for i in range(len(alllist)):   # banned_id가 같은 user_id 고르는 것 제외
        toset = set(alllist[i])
        if len(toset) == len(banned_id):
            lastlist.append(list(toset))
    endlist = list(set(map(tuple, lastlist)))   # 순서만 바뀌어 중복된 경우 제외
    answer = len(endlist)
    return answer
