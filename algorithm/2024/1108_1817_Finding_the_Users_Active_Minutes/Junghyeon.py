from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dictionary = defaultdict(set)
        result = [0] * k
        
        # set으로 중복 제거
        for ID, time in logs:
            dictionary[ID].add(time)
        
        # 빈도수에 따라 result 업데이트
        for i in dictionary:
            result[len(dictionary[i])-1] += 1

        return result
