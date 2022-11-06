class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)
        seen = set()
        answer = []
        
        # 만들수 없으면 return []
        if sum(nums[:4]) > target or sum(nums[-4:]) < target :
            return []

        # 각 자릿수에서
        # 현상태로부터 만들 수 있는 최솟값이 target 보다 크면 break
        # 현상태로부터 만들 수 있는 최댓값이 target 보다 작으면 continue
        # 현상태의 값으로 부터 마지막의 도달한값이 봤던 값이면 continue
        for i in range(len(nums)-3):
            a = nums[i]
            if sum(nums[i+1:i+4]) + a > target:
                break
            if sum(nums[-3:]) + a < target:
                continue
            if tuple([a, nums[-3], nums[-2], nums[-1]]) in seen:
                continue
            for j in range(i+1, len(nums)-2):
                b = nums[j]
                if sum(nums[j+1:j+3]) + a + b > target:
                    break
                if sum(nums[-2:]) + a + b < target:
                    continue
                if tuple([a, b, nums[-2], nums[-1]]) in seen:
                    continue
                for k in range(j+1, len(nums)-1):
                    c = nums[k]
                    if sum(nums[k+1:k+2]) + a + b + c > target:
                        break
                    if sum(nums[-1:]) + a + b + c < target:
                        continue
                    if tuple([a, b, c, nums[-1]]) in seen:
                        continue
                    for l in range(k+1, len(nums)):
                        d = nums[l]
                        if  a + b + c + d > target:
                            break
                        if  a + b + c + d < target:
                            continue
                        if tuple([a, b, c, d]) in seen:
                            continue
                        # 합이 target값돠 동일해지면 answer에 추가
                        if a + b + c + d == target:
                            seen.add(tuple([a, b, c, d]))
                            answer.append([a, b, c, d])

        return answer
