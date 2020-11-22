class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        path = []
        answer = -1
        for i in range(len(nums)):
            if i in path:                        # 이미 갔던 곳이라면 패스
                pass
            path.append(i)                       # 왔던 곳 저장
            temp = 1
            next_path = nums[i]
            while next_path not in path:         # 다음 곳이 왔던 곳이 될 때까지
                path.append(next_path)           # 지금 있는 곳 저장
                temp += 1                        
                next_path = nums[next_path]      # 다음 곳으로 이동
            if answer < temp:             
                answer = temp
            if answer > len(nums)/2:             # 전체 길이의 절반 이상이라면 break
                break
        return answer
