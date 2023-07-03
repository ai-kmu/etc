# sliding window
# l: left, r: right

class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        # 현재 window에 있는 숫자들 저장.
        # 같은 숫자가 여러 번 나올 수 있기 때문에 set이 아닌 dict이용
        window = dict()

        l = 0
        for r, n in enumerate(nums):
            # 현재 window에 있는 숫자 업데이트.
            # 없는 경우를 위해 get method 이용
            window[n] = window.get(n, 0) + 1

            # 문제 조건인 최대 최소 차이가 2보다 클 때까지
            while max(window) - min(window) > 2:
                left = nums[l]
                # 숫자 걸러내기
                window[left] -= 1
                if not window[left]:
                    del window[left]
                l += 1
            
            # 현재 window에서 가능한 subarray 개수
            answer += (r - l) + 1

        return answer
