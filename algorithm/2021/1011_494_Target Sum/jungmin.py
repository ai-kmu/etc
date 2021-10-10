class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:  
        
        @cache
        def caculate(i, sums):
            # 재귀적으로 현재 인덱스 값에서 다음 인덱스의 값을 더하거나 빼는 함수
            # 다만 위에 @cache를 선언해야 중복 연산을 안하여 time limit 오류가 안나옴
            
            if i == len(nums): # nums만큼 다 더했을 때 target과 같으면 1, 아니면 0 출력
                if sums == target:
                    return 1
                else:
                    return 0

            else:
                # nums 길이 만큼 아직 다 더하지 않았다면 카운트 세는 cnt를 0으로 초기화 하고 반복적으로 다음 값을 더하거나 뺀다.
                cnt=0
                cnt+=caculate(i+1, sums + nums[i])
                cnt+=caculate(i+1, sums - nums[i])
        
            return cnt
        
        return caculate(0, 0) # 인덱스 0의 값에서부터 반복적으로 더하여 최종 갯수를 구한다.
