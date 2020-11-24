class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        answer = 0
        # 이전에 봤던 인덱스인지 아닌지 확인
        visited = set()
        for i in range(len(nums)):
            temp = 0
            # 이전에 보지 않았던 경우에 대해서면 나올 수 있는 경우를 구함
            while not i in visited:
                temp += 1
                visited.add(i)
                i = nums[i]
            answer = max(answer, temp)
        return answer

