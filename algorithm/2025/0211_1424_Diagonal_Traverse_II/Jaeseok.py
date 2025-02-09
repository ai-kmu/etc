from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        answer = []
        diagonal = defaultdict(list)

        # row와 col의 합이 같다 = 같은 대각선 상에 있다
        # defaultdict 안에 같은 대각선 상에 있는 값들을 저장
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonal[i+j].append(nums[i][j])

        # defaultdict 안에 대각선 값은 작은 순서대로 저장되어 있으므로 순서 유지
        # 그러나 각 리스트 안에 있는 값은 역순으로 되어 있으므로 뒤집어줌
        for l in diagonal.values():
            for v in l[::-1]:
                answer.append(v)

        return answer
