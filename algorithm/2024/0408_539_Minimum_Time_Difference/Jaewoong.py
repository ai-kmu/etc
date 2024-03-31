# 시간:분 을 분으로 통일해서 리스트에 넣어줌
# 그러나 반대로 계산해야 되는 경우도 있음(시간은 순환되기 때문)
# 반대로 계산되는 부분은 24시간에서 빼줌으로서 계산
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        timePoints = sorted(timePoints)
        time_int = []
        time_int_rev = []
        time_diff = []
        # 시간:분을 인덱싱 후 분으로 환산
        # 정방향으로 계산된 시간은 time_to_int
        # 역방향으로 계산된 시간은 time_int_rev
        for i in timePoints:
            hour = i[0:2]
            minute = i[3:5]
            time_to_int = int(hour)*60 + int(minute)
            time_int.append(time_to_int)
            time_int_rev.append(1440 - time_to_int)
        

        time_int_rev = sorted(time_int_rev)
        # 최소 시간을 계산하기 위해 정방향에서 옆의 시간과 빼어 time_diff에 저장
        # 역방향에서 계산하기 위해서는 정방향의 수와 역방향의 수를 더함
        for i in range(len(time_int)):
            time_diff.append(time_int[i]+time_int_rev[i])
            if i==len(time_int)-1:
                break
            else:
                time_diff.append(time_int[i+1] - time_int[i])
        
        # 최종적으로 계산된 값들의 최솟값 리턴
        return min(time_diff)
