# 풀다가 답 봐버렸어요 리뷰 안해주셔도 돼요

from collections import defaultdict

class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # 사용자별 고유 시간 저장을 위한 딕셔너리 생성
        user_minutes = defaultdict(set)
        
        # 각 사용자의 고유 활동 시간을 집합에 추가하여 중복 시간 제거
        for user_id, time in logs:
            user_minutes[user_id].add(time)
        
        # 각 사용자별 UAM을 카운트하는 딕셔너리 생성
        uam_count = defaultdict(int)
        for minutes in user_minutes.values():
            uam = len(minutes)  
            uam_count[uam] += 1
        
        # 결과 배열 생성, 크기는 k로 설정
        answer = [0] * k
        for i in range(1, k + 1):
            answer[i - 1] = uam_count[i]
        
        return answer
