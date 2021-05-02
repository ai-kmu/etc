class Solution:
    def insert(self, itvs: List[List[int]], new_itv: List[int]) -> List[List[int]]:
        if len(itvs)==0:            # itvs 0인 경우
            return [new_itv]
        ans = []
        new_0, new_1 = new_itv[0], new_itv[1]
        temp = -1
        for idx, itv in enumerate(itvs): # 오름차순이므로 탐색하면서 구간 겹치기 할수있음
            if itv[1] < new_itv[0]:      # 안 겹치는 경우
                ans.append(itv)
                continue
            elif itv[0] > new_itv[1]:    # new_itv 구간 지나간 경우
                temp = idx
                break
            
            # print(itv[0], new_itv[0])  # 겹치는경우 구간 갱신
            new_0 = min(itv[0], new_0)
            new_1 = max(itv[1], new_1)
        
        ans.append([new_0, new_1])
        if temp>-1:
            ans += itvs[temp:]
        return ans
        
