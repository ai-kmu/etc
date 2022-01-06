# dp로품(점화식 사용)
# days[0]날짜까지의 최소 비용은 costs[0]
# days[:i]날짜까지의 최소 비용은 min(days[i] -30 + costs[2], days[i] -7 + costs[1], days[i] + costs[0])
# 위 점화식을 마지막 날짜까지 진행

class Solution:
    def mincostTickets(self, days, costs):
        calender = [0] * (days[0]+30)  # 30일 이전을 볼 때 예외처리 하기 싫어서 30일부터 시작
        days += [days[-1]+1]  # 마지막거 예외처리 하기 싫어서 days를 하나 늘려줌

        for i in range(len(days)-1):
            # calender에 days[i]~days[i+1]까지 최소비용을 저장함
            calender += [min(calender[days[i]]    + costs[2], 
                             calender[days[i]+23] + costs[1],
                             calender[days[i]+29] + costs[0])] * (days[i+1]-days[i])  

        return calender[-1]
