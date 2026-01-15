# 597 / 689 testcases passed
# 풀이 실패 TC 존재함

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        num_of_meetings = len(startTime)
        print(num_of_meetings)  
        gaps_list = []

        gaps_list.append(startTime[0])

        for i in range(1, num_of_meetings):
            gaps_list.append(startTime[i] - endTime[i-1])
        
        gaps_list.append(eventTime - endTime[num_of_meetings-1])

        window_size = k + 1
        current_sum = 0
        for i in range(window_size):
            current_sum = current_sum + gaps_list[i]

        max_val = current_sum

        for i in range(1, len(gaps_list) - window_size):
            adding_gap = gaps_list[i + k]
            removing_gap = gaps_list[i - 1]

            current_sum = current_sum + adding_gap - removing_gap

            max_val = max(max_val, current_sum)

        return max_val
