class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        nums.sort()
        
        # 두 개의 숫자를 먼저 더해서 값을 계산한 후에
        # 양쪽에 숫자를 하나씩 설정하여 합을 구해 타겟이 나올 때까지
        # 범위를 줄여가며 탐색
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                # 먼저 첫 번째 합을 구해준다
                # 이 후 j index이후의 양끝 인덱스의 숫자를 고른다
                first_sum = nums[i] + nums[j]
                left = j + 1
                right = len(nums) - 1
                
                # left가 right보다 작아질때까지 범위를 줄여가며 이분 탐색을 한다
                while left < right:
                    # 처음 더한 것에 left, right index의 숫자를 더해주어서 최종 합을 구한다
                    final_sum = first_sum + nums[left] + nums[right]
                    
                    # 만약 최종 합이 target과 같다며 정답에 값을 더해준다
                    # 그리고 left는 한칸 뒤로 이동하고 right는 한 칸 앞으로 이동한다
                    if final_sum == target:
                        answer.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        
                    # 만약 최종 합이 타겟보다 작다면 left의 수를 늘려 합을 크게 키워준다
                    elif final_sum < target:
                         left += 1
                    else:
                         right -= 1
                            
        return answer
    
