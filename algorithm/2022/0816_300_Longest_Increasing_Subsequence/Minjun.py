class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        '''
        subseq 끝 값보다 현재 nums[i]가 크면 부분수열에 넣는다.
        subseq 끝 값보다 현재 nums[i]가 작으면, 이진 탐색으로 집어 넣는다.
        -> 이전에 있는 값 중에 현재 값보다 큰 값 중 제일 작은 값을 대체한다
        '''
        
        n = len(nums)
        # subseq nums[0]으로 생성
        subseq = [nums[0]]
        
        # nums[0] 제외 ~n 비교
        for i in range(1,n):
            # subseq 끝 값보다 크면, 추가
            if nums[i] > subseq[-1]:
                subseq.append(nums[i])
            # subseq 끝 값보다 작으면, 비교
            else:
                left = 0
                right = len(subseq)
                
                # 이분탐색
                while left < right:
                    middle = (left + right) // 2
                    if nums[i] > subseq[middle]:
                        left = middle + 1
                    else:
                        right = middle
                subseq[right] = nums[i]
                
        return len(subseq)
                    
