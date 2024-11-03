class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        '''
        log_id
            key: ID
            value: log for each ID (type: dict)
                key: time
                value: True
        '''
        log_id = dict()
        ans = [0] * k

        for log in logs:
            user_id, time = log
            try:  # 해당 id에 대한 dict이 사전에 정의되었는 지 확인
                log_id[user_id]
            except:  # 없다면 새로 선언
                log_id[user_id] = dict()
            log_id[user_id][time] = True  # 해당 id가 주어진 time에 action을 수행했음을 기록

        for user_id in log_id.keys():  # 기록된 id 별로 UAM 계산
            ans[len(log_id[user_id].keys())-1] += 1

        return ans
