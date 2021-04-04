class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        ans = [1 for i in range(len(rains))]                # 0인 날에 비울 호수가 없다면 1 <=> 10^9 숫자만 반환하면 되기 때문에 1로 초기화 
        to_dry = []                                         # 비워야 하는 호수의 index
        
        check = set()                                       # 가득 찬 호수의 번호 저장
        for idx, lake in enumerate(rains):        
            if lake in check and lake != 0:                 # 비가 온 호수이면서 이미 가득 찬 호수인 경우
                to_dry.append(idx)                          # 비워야 하는 호수에 저장
            else:                                           # 가득 차지 않은 호수인 경우 
                check.add(lake)                             # 가득 찬 호수에 저장
            
        full = set()                                        # 현재까지 가득 찬 호수를 저장
        for idx, lake in enumerate(rains):
            if lake:                                        # 비가 내리는 날인 경우
                if lake in full:                            # 만약 가득 채워진 호수인 경우
                    return []                               # 홍수가 나기 때문에 빈 리스트 반환
                full.add(lake)                              # 아닌 경우 현재까지 가득 찬 호수에 저장
                ans[idx] = -1                               # 정답 리스트에 -1로 저장
            else:                                           # 비가 내리지 않는 날인 경우
                for dry_idx, dry_lake in enumerate(to_dry): 
                    if rains[dry_lake] in full:             # 현재까지 가득찬 호수 중에 뒤에 비가 또 내릴 호수를 찾아서
                        day = to_dry.pop(dry_idx)           
                        ans[idx] = rains[day]               # 정답 리스트에 그 호수 번호 저장
                        full.remove(rains[day])             # 현재까지 가득찬 호수에서 삭제
                        break    
        return ans
