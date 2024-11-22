class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        
        total_time = 0
        for i in range(len(timeSeries)):
            posion_time = timeSeries[i] + duration
            # 마지막이 아니고
            if i != len(timeSeries)-1:
                # posion_time이 적어야 시작
                if posion_time < timeSeries[i+1]:
                    total_time += duration
                else:
                    total_time += timeSeries[i+1]-timeSeries[i]
            else:
                total_time += duration
        return total_time
                
            
