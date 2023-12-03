# 2차 제출 11:58
# 풀이 하나 더 떠올랐는데 시간 없어서 일단 제출 - 는 아니었음
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

# 아이디어: 홀수 번째 합 == 짝수 번째 합 -> 11의 배수
# 반례: 11의 배수는 abs(홀수 번째 합 - 짝수 번째 합) = 11의 배수이면 된다. 0이어야할 필요가 없다.
# [4, 1, 1, 2, 5, 1, 5, 4]에서 마지막 4를 지운 4112515는 11의 배수이지만 홀수의 합과 짝수의 합이 다르다.
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        # 초기: 왼쪽엔 아무것도 없고 오른쪽에 다 넣어둔 상태
        left = ''
        right = ''.join(str(n) for n in nums)
        
        answer = 0
        for n in nums:
            # 오른쪽 앞에 거 하나 빼서
            right = right[1:]
            # 확인하고
            temp = left + right 
            answer += bool(not int(temp) % 11)  # 11의 배수이면 0, 거기 not을 붙여서 1 더함
            # 왼쪽에 도로 붙이기
            left += str(n)
        return answer
