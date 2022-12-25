class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # nums를 cost와 함께 정렬함
        sorted_nums = sorted(zip(nums, cost))
        total_cost = sum(cost)
        curr_cost = 0

        # 총 cost를 최소화 하려면 cost가 큰 것을 적게 조작하여 target 숫자로 바꿔야한다
        # sorted_nums는 nums기준으로 정렬되어 있기 때문에
        # 순서대로 반복문을 돌며 현재 cost를 계속 더하여 생긴 cost가 총 cost의 절반보다 큰 순간
        # 해당 num을 target으로 하여 cost를 계산한다.
        for num, c in sorted_nums:
            curr_cost += c
            if curr_cost > (total_cost // 2):
                target = num
                break
        
        answer = 0

        # 총 cost 계산

        for num, c in sorted_nums:
            answer += c * abs(num - target)
        
        return answer
