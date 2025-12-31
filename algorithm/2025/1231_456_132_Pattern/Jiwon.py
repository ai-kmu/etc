# 솔루션 참고

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # second 후보
        third: int = float('-inf')  # third를 위한 최댓값 저장 변수
        
        # j < k 조건 만족을 위해 오른쪽에서 왼쪽으로 확인
        for num in reversed(nums):
            if num < third:
                return True

            # pop 되는 요소는 현재 num 오른쪽에 위치 > third 가능
            while stack and stack[-1] < num:
                third = stack.pop()
            # 현재 num을 stack에 push > second 후보
            stack.append(num)

        return False
