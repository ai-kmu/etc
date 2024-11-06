from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # id별 uam을 위한 id:set defaultdict 선언
        uam_per_id = defaultdict(set)
        
        # answer list 선언
        answer = [0] * k

        # set.add로 id_i set에 time_i 추가
        for id_i, time_i in logs:
            uam_per_id[id_i].add(time_i)

        # id별 uam 개수 answer[length - 1]에 count
        for n_uam in uam_per_id.values():
            length = len(n_uam)
            answer[length - 1] += 1

        return answer
