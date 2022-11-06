class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # nums 정렬
        ans = set() # 정답 저장 set
        
        # 처음에는 nums 첫번째 index부터 세번째 index까지는 순서대로 숫자를 더함
        # 네번째 index는 처음에는 맨 마지막 index에 있는 값을 사용
        # 더하다가 target과 일치하면 그 숫자 조합을 ans에 저장하면서
        # 세번째 index는 하나씩 올리고 네번째 index는 하나씩 떨어트림
        # 만약 더한 결과가 target보다 작으면 세번째 index를 하나씩 올리고
        # 반대로 크면 네번째 index를 하나씩 내린다.
        # 이러한 과정을 반복하여 결과를 출력
        for i in range(len(nums)-3): # i는 첫번째 숫자 index
            for j in range(i+1, len(nums)-2): # j는 두번째 숫자 index
                k = j+1 # 세번째 숫자 index
                l = len(nums)-1 # 네번째 숫자 index
                while k < l:
                    if (nums[i] + nums[j] + nums[k] + nums[l]) == target:
                        ans.add((nums[i],nums[j],nums[k],nums[l]))
                        k += 1
                        l -= 1
                    elif (nums[i] + nums[j] + nums[k] + nums[l]) < target:
                        k += 1
                    else:
                        l -= 1
        return ans
