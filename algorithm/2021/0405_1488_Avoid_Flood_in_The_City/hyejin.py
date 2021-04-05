class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        # rain[i] == 0이면 하나의 lake를 dry할 수 있음
        # flood를 막지 못하면 empty array를 반환
        ans = [1] * n
        dry_idx_arr = [] # dry시킬 수 있는 idx 위치를 저장할 array
        fulled_lake = collections.defaultdict(int) # integer dictionary를 초기화
        
        for i, nth_lake in enumerate(rains):
            if rains[i] == 0:
                dry_idx_arr.append(i) # dry시킬 수 있는 idx
    
            else:
                if nth_lake in fulled_lake:
                    if not dry_idx_arr: # dry_idx가 없으면 못 빼므로 flood됨
                        return []
                    
                    # fulled lake의 idx보다 큰 dry_idx가 있는지 탐색
                    idx = None
                    for j in range(len(dry_idx_arr)):
                        if fulled_lake[nth_lake] < dry_idx_arr[j]:
                            idx = j
                            break
                    
                    if idx is None: # 만약 fulled lake의 idx를 뺄 수 있는 dry_idx가 없을 경우엔 flood되므로 [] 반환
                        return []
                    
                    dry_idx = dry_idx_arr[idx] # 가능하다면 dry_idx를 가져옴
                    ans[dry_idx] = nth_lake
                    
                    dry_idx_arr.pop(idx) # 사용한 dry_idx를 뺌
                
                fulled_lake[nth_lake] = i # lake를 업데이트 시킴
                ans[i] = -1
                
        return ans
                
        
