"""
실패
"""

def solution(user_id, banned_id):
    answer = set()
    user_list, pos_list = list(), list()
    for j in range(len(banned_id)):
        temp = []
        for user in user_id:
            correct = False
            num = len(banned_id[j])
            
            #길이가 다르면 아이디가 같을 수 없음
            if num != len(user):
                continue
            
            #만약 모든 글자가 *로 이루어졌다면 길이가 같으면 어떤 아이디던 가능
            if banned_id[j] == "*" * num:
                temp.append(user)
                pass
            
            #각 char를 비교하면서 만약 하나라도 다르면 False 모두 같으면 True
            #모두 같을 경우는 따로 저장해둠
            for i in range(num):
                if banned_id[j][i] == '*':
                    continue
                if banned_id[j][i] != user[i]:
                    correct = False
                    break
                correct = True
            if correct == True:
                temp.append(user)
        pos_list.append(temp)   
        
    print(pos_list)
    num = len()
    
