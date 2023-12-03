class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        # 인덱스가 홀수일 때, 짝수일 때 각각의 list에 누적합
        even_sum = [nums[0]]
        odd_sum = [0]
        # 인덱스가 홀수(짝수)일 때 짝수(홀수) 누적합 list는 전 누적합을 그대로 저장
        for i in range(1, n):
            if i % 2 == 0:
                even_sum.append(even_sum[-1] + nums[i])
                odd_sum.append(odd_sum[-1])
            else:
                odd_sum.append(odd_sum[-1] + nums[i])
                even_sum.append(even_sum[-1])
        # 첫 번째를 돌 때를 위해 마지막에 0을 추가
        odd_sum.append(0)
        even_sum.append(0)
        # 현재 인덱스의 숫자를 뺀다면 그 뒤의 인덱스의 홀수가 바뀜
        # 홀수(짝수)는 전까지의 누적합과 나머지 짝수(홀수) 뒷 부분의 나머지 누적합을 얻게 됨
        # 이 둘이 같다면 fair하므로 answer에 추가
        for i in range(n):
            odd_cal = odd_sum[i - 1] + even_sum[-2] - even_sum[i]
            even_cal = even_sum[i - 1] + odd_sum[-2] - odd_sum[i]
            if odd_cal == even_cal:
                answer += 1
        return answer
