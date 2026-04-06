class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # arrival time과 total time 비교, arrival이 total보다 길면 arrival로 갱신하고 대기 시간 계산
        total_t = 0
        ret = 0
        for a_i, t_i in customers:
            total_t = max(total_t, a_i) + t_i
            ret += (total_t - a_i)
        return ret / len(customers)
