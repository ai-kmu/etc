# 솔루션 참고... 다음 주부터는 진짜 풀게요...

import math
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        count_dict = {}
        total_days = 0
        for task in tasks:
            if task not in count_dict:
                count_dict[task] = -math.inf
            total_days = max(total_days + 1, count_dict[task] + space + 1)
            count_dict[task] = total_days
        return total_days
