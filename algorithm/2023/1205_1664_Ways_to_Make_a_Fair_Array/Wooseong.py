# 1차 제출 11:48
# 풀이 하나 더 떠올랐는데 시간 없어서 일단 제출
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # 초기 짝수, 홀수 합
        sum_eve = sum(nums[0::2])
        sum_odd = sum(nums[1::2])
        
        # 정답값 init
        answer = 0
        for i, n in enumerate(nums):
            # 홀수 번째 애를 뽑을 차례니까
            if i % 2:
                sum_odd -= n                    # 홀수에서 빼놓고
                answer += (sum_odd == sum_eve)  # 같은지 확인하고
                sum_eve += n                    # 짝수에 더해 놓기
            
            # 짝수 번째 애를 뽑을 차례면
            else:
                sum_eve -= n                    # 짝수에서 빼놓고
                answer += (sum_odd == sum_eve)  # 같은지 확인하고
                sum_odd += n                    # 홀수에 더해 놓기

        return answer   # 같았던 만큼 반환됨
