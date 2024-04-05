class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def time_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(':'))
            return hours * 60 + minutes

        # 시간을 분으로 변환하여 리스트에 저장
        time_in_minutes = [time_to_minutes(time_str) for time_str in timePoints]
        # 시간을 정렬
        time_in_minutes.sort()
        # 최소 시간 차이를 저장하기 위한 변수
        min_diff = float('inf')  
        
        # 각 시간 간의 차이 계산
        for i in range(len(time_in_minutes) - 1):
            diff = time_in_minutes[i + 1] - time_in_minutes[i]
            min_diff = min(min_diff, diff)

        # 첫 번째 시간과 마지막 시간의 차이도 고려
        # 시계는 원형이므로 마지막 시간과 첫 번째 시간의 차이도 고려되어야 함
        diff_between_ends = (24 * 60 - time_in_minutes[-1]) + time_in_minutes[0]
        min_diff = min(min_diff, diff_between_ends)

        return min_diff
