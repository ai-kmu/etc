class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = 0
        total_wait = 0
        
        for arrival, duration in customers:
            start_time = arrival if cur_time < arrival else cur_time
            
            finish_time = start_time + duration
            total_wait += (finish_time - arrival)
            
            cur_time = finish_time
            
        return total_wait / len(customers)
