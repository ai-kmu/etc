class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cumulative_time = 0
        wait_time = []

        for i in range(len(customers)):
            # chef가 아직 이전 요리를 하고 있거나 방금 끝난 경우
            if cumulative_time >= customers[i][0]:
                cumulative_time += customers[i][1]

            # chef가 쉬고 있는 경우
            else:
                cumulative_time = customers[i][0] + customers[i][1]
            
            # 고객의 총 대기 시간
            wait_time.append(cumulative_time - customers[i][0])
        
        return sum(wait_time) / len(customers)
