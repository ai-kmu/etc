class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
               
        dic = collections.defaultdict(list)
        ans = [-1] * len(rains)
        full_lake = set([])  # 현재 full인 lake, 중복제거를 위해 set 사용
        about_to_flood = [] # 값이 두번 이상 나온 dry 해야할 lake index

        for day, lake in enumerate(rains): 
            dic[lake].append(day)

        for i in range(len(rains)):
            lake = rains[i]
            
            if lake: # lake가 0이 아닐경우
                if lake in full_lake: # lake가 이미 full에 있을 경우 종료
                    return []
                full_lake.add(lake) # full_lake에 해당 lake index 추가
                dic[lake].pop(0) # dry일 때 제거해야할 lake index인지 판단을 위해 해당 lake번호를 딕셔너리에서 제거
                if dic[lake]: # 제거하고도 lake가 남아있을 경우는 dry일 때 제거해야 함
                    heapq.heappush(about_to_flood, dic[lake][0])
                    
            else:  # lake가 0일 경우
                if about_to_flood:  #처리해야할 lake가 있을 경우 dry시킨다
                    ans[i] = rains[heapq.heappop(about_to_flood)]
                    full_lake.remove(ans[i]) # 처리된 lake는 full_lake에서 제거
                else:  # 처리해야 할 lake가 없을 경우
                    ans[i] = 1
            
        return ans
