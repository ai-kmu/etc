class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # 풀기 실패해서 정답 봤습니다.
        # 리뷰 안해주셔도 됩니다.

        # 필요한 변수 선언
        # total이 최종 정답 값
        # 왼쪽은 인덱스 0부터 시작
        n, total, left, dict_ = len(nums), 0, 0, defaultdict(int)
        for right in range(n):
            dict_[nums[right]] += 1

            # dict에 있는 key값들 중 최대와 최소값 간 차이가 2보다 크면
            # nums의 left에 있는 키값을 -1 줄임
            while max(dict_.keys()) - min(dict_.keys()) > 2:
                dict_[nums[left]] -= 1
                # 
                if dict_[nums[left]] == 0:
                    del dict_[nums[left]]
                left += 1
            total += right-left+1
        return total
