# 틀린 풀이
# 2 / 34 testcases passed
# 풀이 안해주셔도 됩니다. 

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        list_len =[] # interval value를 저장할 list
        length = len(intervals)
        for i in range(length):
            tmp =[]
            tmp.append(intervals[i][1] - intervals[i][0])
            tmp.append(i)
            list_len.append(tmp)

        # 두 번째 차원의 앞의 원소를 기준으로 정렬 -> interval value를 기준으로 정렬
        sorted_list = sorted(list_len, key=lambda x: x[0])

        ans = length
        for i in range(length-1, -1, -1):
            for j in range(i-1, -1, -1):
                l_idx = sorted_list[j][1]
                r_idx = sorted_list[i][1]
                if intervals[l_idx][0] >= intervals[r_idx][0] and intervals[l_idx][1] <= intervals[r_idx][1]:
                    ans = ans -1
                    break

        return ans
        
