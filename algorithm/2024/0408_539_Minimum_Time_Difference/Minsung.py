class Solution:
    def findMinDifference(self, timePoints) -> int:
        time_list = list()
        for timePoint in timePoints:
            h, m = map(int, timePoint.split(':'))
            time_list.append([h, m])  # 24:59 -> [24, 59]

        time_list.sort(key = lambda x : (x[0], x[1]))
        time_list.append(time_list[0])  # 정렬된 배열의 가장 앞과 뒤와 비교하기 위해 추가 
        
        ans = 60 * 25  # 최대값 정의 
        
        for i in range(len(time_list[1:])):
            h_1, m_1 = time_list[i]
            h_2, m_2 = time_list[i+1]

            if i == len(time_list) - 2:
                h_1, m_1, h_2, m_2 = h_2, m_2, h_1, m_1
            
            diff = min(60*h_2 + m_2 - 60*h_1 - m_1, 60*(h_1+24) + m_1 - 60*h_2 - m_2)
            ans = min(ans,diff)

        return ans
