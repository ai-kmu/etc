class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        목표: 빈 시간들의 최대 합을 찾으면 됨
        """
        # 빈 시간 저장 배열
        # 첫 회의랑 마지막 회의 앞뒤 시간도 더해야 함
        freeTime = [startTime[0]]
        for i in range(1, len(startTime)):
            freeTime.append(startTime[i] - endTime[i - 1])
        freeTime.append(eventTime - endTime[-1])

        freeTimeSum, ans = 0, 0
        for i in range(len(freeTime)):
            freeTimeSum += freeTime[i]
            # 최대 합 찾아야 하니까 reschedule 횟수 고려
            if i >= k:
                ans = max(freeTimeSum, ans)
                freeTimeSum -= freeTime[i - k]  # 윈도우 벗어나면 지우고 새로운 애 받아야 함(line 15)
        
        return ans

