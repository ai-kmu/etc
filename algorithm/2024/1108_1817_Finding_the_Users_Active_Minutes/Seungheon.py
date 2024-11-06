class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        # 활성시간이 n 분인 사람의 수를 count

        answer =  [0]*k

        # id 마다 시간 저장, set으로 중복 제거
        id_time_dict = {}
        for id_idx, time_idx in logs:
            if id_idx in id_time_dict.keys():
                id_time_dict[id_idx].add(time_idx)
            else:
                id_time_dict[id_idx] = set([time_idx])

        # 사람별로 time 가져오기  
        for time_log in id_time_dict.values():
            answer[len(time_log)-1] += 1
        
        return answer
