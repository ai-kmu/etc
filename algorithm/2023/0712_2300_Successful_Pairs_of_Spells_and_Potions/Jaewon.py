class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        # potions 거꾸로 정렬하면 속도 개선될 것
        potions.sort(reverse=True)
        answer = []

        for i in range(len(spells)):
            left, right = 0, len(potions) - 1  # 이분탐색 위함
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] * spells[i] >= success:  # 조건 만족시
                    left = mid + 1  # 오른쪽 탐색 위함
                else:
                    right = mid - 1  # 왼쪽 탐색 위함
            answer.append(left)
        return answer
