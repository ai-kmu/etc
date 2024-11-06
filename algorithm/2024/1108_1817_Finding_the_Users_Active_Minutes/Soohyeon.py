# 솔루션 참조
class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        
        # UAM을 저장할 리스트
        ret = [0] * k  
        # 사용자의 활동 시간 저장
        user_acts = {}  
        
        #각 사용자 ID에 대해 User_acts 딕셔너리에 분을 추가함.
        for log in logs:
            # 만약 이미 ID가 존재하면 해당 분을 리스트에 추가하고, 존재하지 않으면 새로운 리스트를 생성
            if user_acts.get(log[0], 0):
                user_acts[log[0]].append(log[1])
            else:
                user_acts[log[0]] = [log[1]]
                
        # 시간 중복 제거
        # 고유한 활동 분수를 측정(len)하여 ret에 업데이트
        for k, v in user_acts.items():
            l = len(set(v))
            ret[l-1] += 1

        return ret